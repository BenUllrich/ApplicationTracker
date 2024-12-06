from tkinter import Tk, Label, Entry, Button, OptionMenu, StringVar, messagebox
from tkinter import Toplevel, ttk
from datetime import date
import csv
import pandas as pd
import matplotlib.pyplot as plt
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

def submit_application():
    company = company_var.get()
    title = title_var.get()
    platform = platform_var.get()
    status = status_var.get()
    submission_date = date.today()
    conn = conn_var.get()

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
       
"""
def view_applications():
 Maybe lets use treeview for this one
"""

"""
def show_analytics():
 Dave -- use pandas or matplotlib
"""
# GUI setup
root = Tk()
root.title("JobApplications")

Label(root, text="Company").grid(row=0, column=0)
company_var = StringVar()
Entry(root, textvariable=company_var).grid(row=0, column=1)

Label(root, text="Job Title").grid(row=1, column=0)
title_var = StringVar()
Entry(root, textvariable=title_var).grid(row=1, column=1)

Label(root, text="App Platform").grid(row=2, column=0)
platform_var = StringVar()
Entry(root, textvariable=platform_var).grid(row=2, column=1)

Label(root, text="Application Status").grid(row=3, column=0)
status_var = StringVar()
OptionMenu(root, status_var, "Submitted", "Interviewing", "Offer Received", "Rejected").grid(row=3, column=1)

Label(root, text="Connections").grid(row=4, column=0)
conn_var = StringVar()
Entry(root, textvariable=conn_var).grid(row=4, column=1)

Button(root, text="Submit", command=submit_application).grid(row=5, column=0, columnspan=2)


root.mainloop()
