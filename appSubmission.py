from tkinter import messagebox
from datetime import date
import csv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


# Google Drive Authentication
def authenticate_user():
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return build('drive', 'v3', credentials=creds)

def upload_to_drive(file_name):
    try:
        service = authenticate_user()
        file_metadata = {'name': file_name}
        media = MediaFileUpload(file_name, mimetype='text/csv')
        service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        messagebox.showinfo("Success", "File uploaded to Google Drive!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to upload to Google Drive: {str(e)}")

def submit_application(app):
    submission_date = date.today()

    if not app.getCompany() or not app.getTitle() or not app.getPlatform() or not app.getStatus():
        messagebox.showerror("Error", "All fields except 'Connections' are required!")
        return

    file_name = "applications.csv"
    try:
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([app.getCompany(), app.getTitle(), app.getPlatform(), app.getStatus(), submission_date, app.getConn()])
        messagebox.showinfo("Success", "Application added successfully!")
        upload_to_drive(file_name)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save application: {str(e)}")
       
"""
def view_applications():
 Maybe lets use treeview for this one
"""

"""
def show_analytics():
 Dave -- use pandas or matplotlib

"""
