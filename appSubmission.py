from tkinter import messagebox
from datetime import date
import csv
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


# Google Drive Authentication
def authenticate_user():
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


def submit_application(app, fileName):
    """
    Add an application to the local CSV
    :param app: Instance of application object to be added
    :return:
    """

    file_name = fileName
    submission_date = date.today() # using current date to accurately update

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


