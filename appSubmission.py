from tkinter import messagebox
from datetime import date
import csv
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload  
from googleapiclient.http import MediaIoBaseDownload

import matplotlib.pyplot as plt
from io import BytesIO


# Google Drive Authentication
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


def checkCSV(file_name):
    """
    Check if the local CSV file exists, if not, create one:

    :param file_name: name of CSV file to check for
    :return:
    """
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            if file.readline() != 'Company,Position,Source,Status,Date,Contact Person\n':
                with open(file_name,'w') as writeFile:
                    writeFile.write('Company,Position,Source,Status,Date,Contact Person\n')
    else:
        with open(file_name, 'w') as writeFile:
            writeFile.write('Company,Position,Source,Status,Date,Contact Person\n')


# Uploads a file to Google Drive
def upload_to_drive(file_name):
    """
    :param file_name: file to upload
    :return:
    """
    try:
        service = authenticate_user()
        file_metadata = {'name': file_name}
        media = MediaFileUpload(file_name, mimetype='text/csv')
        service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        messagebox.showinfo("Success", "File uploaded to Google Drive!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to upload to Google Drive: {str(e)}")

# Downloads a file from Google Drive and saves it locally
def download_from_drive(service, file_id, local_path):
    """
    Download a file from Google Drive.
    :param service: Authenticated Google Drive service.
    :param file_id: ID of the file to download.
    :param local_path: Path to save the downloaded file.
    """
    request = service.files().get_media(fileId=file_id)
    with open(local_path, 'wb') as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            done = downloader.next_chunk()[1]

# Check and update a file on Google Drive
def check_and_update_drive(file_name, new_entry):
    """
    Check if the file exists on Google Drive, download it if it does,
    update with new data, and re-upload it. If the file doesn't exist,
    create and upload it. 

    :param file_name: Name of the file to check on Google Drive.
    :param new_entry: New data to add to the file.
    """

    service = authenticate_user()
    query = f"name='{file_name}' and mimeType='text/csv'"
    results = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    files = results.get('files', [])

    if files:
        # File exists: Download, update, and re-upload
        file_id = files[0]['id']
        print(f"Found {file_name} in Google Drive with ID: {file_id}")
        
        # Download the file
        request = service.files().get_media(fileId=file_id)
        file_data = BytesIO()
        downloader = MediaIoBaseDownload(file_data, request)
        done = False
        while not done:
            done = downloader.next_chunk()[1]
        file_data.seek(0)

        # Read and update the file locally
        existing_data = list(csv.reader(file_data.read().decode('utf-8').splitlines()))
        
        # Ensure headers exist in the file
        if existing_data[0] != ["Company", "Position", "Source", "Status", "Date", "Contact Person"]:
            existing_data.insert(0, ["Company", "Position", "Source", "Status", "Date", "Contact Person"])
        
        existing_data.append(new_entry)

        # Save updated data locally
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(existing_data)
        
        # Re-upload the updated file
        media = MediaFileUpload(file_name, mimetype='text/csv')
        service.files().update(fileId=file_id, media_body=media).execute()
        print(f"Updated {file_name} and uploaded it back to Google Drive.")

    else:
        # File does not exist: Create locally and upload
        print(f"{file_name} not found. Creating a new file...")
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Company", "Position", "Source", "Status", "Date", "Contact Person"])
            writer.writerow(new_entry)

        # Upload the new file to Google Drive
        upload_to_drive(file_name)

# Adds a new job application
def submit_application(app):
    """
    Add an application to the local CSV
    :param app: Instance of application object to be added
    :return:
    """

    submission_date = date.today()

    if not app.getCompany() or not app.getTitle() or not app.getPlatform() or not app.getStatus():
        messagebox.showerror("Error", "All fields except 'Connections' are required!")
        return

    file_name = "processed_applications.csv"
    new_entry = [
        app.getCompany(), app.getTitle(), app.getPlatform(), app.getStatus(), submission_date, app.getConn()
    ]

    try:
        check_and_update_drive(file_name, new_entry)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process application: {str(e)}")




