from tkinter import Tk, Label, Entry, Button, OptionMenu, StringVar, messagebox
from datetime import date
from googleSheetsAPI import connect_to_google_sheet, add_application_to_sheet
from Application import Application

def submit_application():
    company = company_var.get()
    title = title_var.get()
    resume = resume_var.get()
    cover_letter = cover_letter_var.get()
    platform = platform_var.get()
    status = status_var.get()
    submission_date = date.today()

    try:
        # Create an Application object
        app = Application(
            companyName=company,
            jobTitle=title,
            resumeFile=resume,
            method=platform,
            submissionDate=submission_date,
            coverLetterFile=cover_letter,
            status=status
        )

        # Connect to the Google Sheet
        sheet = connect_to_google_sheet("JobApplications")
        
        # Add the application to the sheet
        add_application_to_sheet(sheet, app)

        messagebox.showinfo("Success", "Application added successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = Tk()
root.title("JobApplications")

Label(root, text="Company").grid(row=0, column=0)
company_var = StringVar()
Entry(root, textvariable=company_var).grid(row=0, column=1)

Label(root, text="Job Title").grid(row=1, column=0)
title_var = StringVar()
Entry(root, textvariable=title_var).grid(row=1, column=1)

Label(root, text="Resume Path").grid(row=2, column=0)
resume_var = StringVar()
Entry(root, textvariable=resume_var).grid(row=2, column=1)

Label(root, text="Cover Letter Path").grid(row=3, column=0)
cover_letter_var = StringVar()
Entry(root, textvariable=cover_letter_var).grid(row=3, column=1)

Label(root, text="Platform").grid(row=4, column=0)
platform_var = StringVar()
OptionMenu(root, platform_var, "LinkedIn", "Company Website", "Other").grid(row=4, column=1)

Label(root, text="Status").grid(row=5, column=0)
status_var = StringVar()
OptionMenu(root, status_var, "Submitted", "Interviewing", "Offer Received", "Rejected").grid(row=5, column=1)

Button(root, text="Submit", command=submit_application).grid(row=6, column=0, columnspan=2)

root.mainloop()
