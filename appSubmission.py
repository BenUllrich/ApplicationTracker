from tkinter import messagebox
from datetime import date
import csv
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from io import BytesIO


# This function helps to log into Google Drive and return the Drive service object
def authenticate_user():
    """
    Authenticates the user with Google Drive using OAuth 2.0.
    Opens a browser window for the user to log in and grant access.
    
    :return: A service object for interacting with Google Drive.
    """
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return build('drive', 'v3', credentials=creds)


# This checks if the CSV file exists locally and makes sure it has the right headers
def checkCSV(file_name):
    """
    Checks if a CSV file exists locally. If it doesn't exist, this function creates it.
    If the file exists but the headers are wrong, it fixes them.

    :param file_name: The name of the CSV file to check or create.
    """
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            if file.readline().strip() != 'Company,Position,Source,Status,Date,Contact Person':
                with open(file_name, 'w') as writeFile:
                    writeFile.write('Company,Position,Source,Status,Date,Contact Person\n')
    else:
        with open(file_name, 'w') as writeFile:
            writeFile.write('Company,Position,Source,Status,Date,Contact Person\n')
            messagebox.showinfo("No file found, creating a fresh CSV file")


# This uploads a file to Google Drive and shows a message when it works
def upload_to_drive(service, file_name):
    """
    Uploads a file to Google Drive. Replaces the file if it exists already. If the upload fails, an error message is shown.

    :param file_name: The name of the file to upload.
    """
    query = f"name='{file_name}' and mimeType='text/csv'"
    results = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    files = results.get('files', [])

    if files:
        # If the file exists on Google Drive, delete the existing file
        file_id = files[0]['id']
        print(f"Trying to replace {file_name} in Drive with ID: {file_id}")
        service.files().delete(fileId=file_id).execute()

    # upload the new file (local csv) to drive, inform the user if this did not happen correctly
    try:
        print(f"Trying to upload new file to drive...")
        metadata = {'name': file_name}  # This is the file name on Google Drive
        media = MediaFileUpload(file_name, mimetype='text/csv')
        service.files().create(body=metadata, media_body=media, fields='id').execute()
        messagebox.showinfo("Success", "File uploaded to Google Drive!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not upload to Google Drive: {str(e)}")


# This function downloads a file from Google Drive and saves it locally
def download_from_drive(service, file_name):
    """
    Downloads a file from Google Drive to the local machine.

    :param service: The authenticated Google Drive service object.
    :param file_name: The name of the file to download.
    """
    print("looking for Google Drive file...")
    query = f"name='{file_name}' and mimeType='text/csv'"
    results = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    files = results.get('files', [])

    if len(files):
        # If the file exists on Google Drive
        file_id = files[0]['id']
        print(f"Found {file_name} in Drive with ID: {file_id}")

        # Download the file
        file_data = BytesIO()
        request = service.files().get_media(fileId=file_id)
        downloader = MediaIoBaseDownload(file_data, request)
        done = False
        while not done:
            done = downloader.next_chunk()[1]
        file_data.seek(0)

        request = service.files().get_media(fileId=file_id)
        with open(file_name, 'wb') as f:
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while not done:
                done = downloader.next_chunk()[1]

        # Read the downloaded file and update it
        existing_data = list(csv.reader(file_data.read().decode('utf-8').splitlines()))
        if existing_data[0] != ["Company", "Position", "Source", "Status", "Date", "Contact Person"]:
            existing_data.insert(0, ["Company", "Position", "Source", "Status", "Date", "Contact Person"])

        # Save the updated data locally
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(existing_data)
    else:
        print("No file found, creating fresh local CSV")


# This was unused as we decided to simply update drive at the end of program execution
"""
# This function handles checking and updating a file on Google Drive
def check_and_update_drive(file_name, new_entry):
    '''
    Checks if a file exists on Google Drive. If it exists, the file is downloaded,
    updated with new data, and uploaded again. If it doesn't exist, the file is created
    and uploaded to Google Drive.

    :param file_name: The name of the file to check and update.
    :param new_entry: The new data to add to the file.
    '''
    service = authenticate_user()
    query = f"name='{file_name}' and mimeType='text/csv'"
    results = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    files = results.get('files', [])

    if files:
        # If the file exists on Google Drive
        file_id = files[0]['id']
        print(f"Found {file_name} in Drive with ID: {file_id}")
        
        # Download the file
        file_data = BytesIO()
        request = service.files().get_media(fileId=file_id)
        downloader = MediaIoBaseDownload(file_data, request)
        done = False
        while not done:
            done = downloader.next_chunk()[1]
        file_data.seek(0)

        # Read the downloaded file and update it
        existing_data = list(csv.reader(file_data.read().decode('utf-8').splitlines()))
        if existing_data[0] != ["Company", "Position", "Source", "Status", "Date", "Contact Person"]:
            existing_data.insert(0, ["Company", "Position", "Source", "Status", "Date", "Contact Person"])
        existing_data.append(new_entry)

        # Save the updated data locally
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(existing_data)
        
        # Upload the updated file to Google Drive
        media = MediaFileUpload(file_name, mimetype='text/csv')
        service.files().update(fileId=file_id, media_body=media).execute()
        print("Updated file uploaded to Google Drive.")
    else:
        # If the file doesn't exist, create it and upload
        print(f"{file_name} not found on Google Drive. Creating a new file...")
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Company", "Position", "Source", "Status", "Date", "Contact Person"])
            writer.writerow(new_entry)
        upload_to_drive(file_name)
"""

def submit_application(app,fileName):
    """
    Adds a job application to the CSV file and updates it on Google Drive.

    :param app: The application object containing job details.
    """
    file_name = fileName
    submission_date = date.today()  # using current date to accurately update

    # ensure data fields are present
    if not app.getCompany() or not app.getTitle() or not app.getPlatform() or not app.getStatus():
        messagebox.showerror("Error", "All fields except 'Connections' are required!")
        return

    # write new row to csv file using application information
    try:
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                [app.getCompany(), app.getTitle(), app.getPlatform(), app.getStatus(), submission_date, app.getConn()])
        messagebox.showinfo("Success", "Applications updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save application: {str(e)}")

