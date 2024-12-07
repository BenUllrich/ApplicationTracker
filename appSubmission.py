from tkinter import Tk, Label, Entry, Button, OptionMenu, StringVar, messagebox
from tkinter import Toplevel, ttk
from datetime import date
import csv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import matplotlib.pyplot as plt
from dataAnalysis import df, status_counts, source_counts, company_counts, applications_timeline, grouped


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

def submit_application(company,title,platform,status,conn=None):
    submission_date = date.today()

    if not company or not title or not platform or not status:
        messagebox.showerror("Error", "All fields except 'Connections' are required!")
        return

    file_name = "applications.csv"
    try:
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([company, title, platform, status, submission_date, conn])
        messagebox.showinfo("Success", "Application added successfully!")
        upload_to_drive(file_name)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save application: {str(e)}")

def show_data_analytics():
    plt.figure(figsize=(8, 6))
    status_counts.plot(kind='bar')
    plt.title('Application Status Count')
    plt.xlabel('Status')
    plt.ylabel('Number of Applications')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 6))
    source_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title("Applications by Source")
    plt.ylabel("")  # Hide y-label for a cleaner look
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    applications_timeline.plot(kind='line', marker='o')
    plt.title("Applications Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Applications")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    grouped.plot(kind='bar', figsize=(12, 8))
    plt.title("Applications Grouped by Status and Source")
    plt.xlabel("Status")
    plt.ylabel("Number of Applications")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
       
"""
def view_applications():
 Maybe lets use treeview for this one
"""


