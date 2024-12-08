from tkinter import *
from tkinter import ttk

import Application
import appSubmission
import pandas as pd


def viewApp(event):
    if lb.curselection():
           companyNameView.config(text="Company: " + apps.loc[lb.curselection()[0], 'Company'])
           jobTitleView.config(text="Position: " + apps.loc[lb.curselection()[0], 'Position'])
           dateView.config(text="Last Updated: " + apps.loc[lb.curselection()[0], 'Date'])
           statusView.config(text="Status: " + apps.loc[lb.curselection()[0], 'Status'])
           platformView.config(text="Last Updated: " + apps.loc[lb.curselection()[0], 'Source'])
           contactView.config(text="Contact: " + apps.loc[lb.curselection()[0], 'Contact Person'])

# Set up the window
window = Tk()
#window.geometry("750x250")
window.title("Application Tracker")
window.resizable(width=False, height=False)
window.size()
window.config(bg="grey16")

tabs = ttk.Notebook(window)
tabs.pack(expand=1)

view = ttk.Frame(tabs)
tabs.add(view, text="View Applications")
add = ttk.Frame(tabs)
tabs.add(add, text="Add New Application")
edit = ttk.Frame(tabs)
tabs.add(edit, text="Update Applications")
analysis = ttk.Frame(tabs)
tabs.add(analysis, text="View Analysis")

# Interface for adding applications:
Label(add, text="Company").grid(row=0, column=0)
company_var = StringVar()
Entry(add, textvariable=company_var).grid(row=0, column=1)

Label(add, text="Job Title").grid(row=1, column=0)
title_var = StringVar()
Entry(add, textvariable=title_var).grid(row=1, column=1)

Label(add, text="App Platform").grid(row=2, column=0)
platform_var = StringVar()
Entry(add, textvariable=platform_var).grid(row=2, column=1)

Label(add, text="Application Status").grid(row=3, column=0)
status_var = StringVar()
status_var.set("Options")
OptionMenu(add, status_var, "Submitted", "Interviewing", "Offer Received", "Rejected").grid(row=3, column=1)

Label(add, text="Connections").grid(row=4, column=0)
conn_var = StringVar()
Entry(add, textvariable=conn_var).grid(row=4, column=1)
(Button(add, text="Submit",
        # create an Application object before submitting it
        command=lambda: appSubmission.submit_application(
            Application.Application(company_var.get(), title_var.get(), platform_var.get(), status_var.get(), conn_var.get())
            )).grid(row=5, column=0, columnspan=2))

# Interface for viewing applications:
lb = Listbox(view, width= 30, height = 15)
apps = pd.read_csv("processed_applications.csv")
for index, row in apps.iterrows():
    lb.insert(index, f"{row['Company']:}  ({row['Date']:>})")


lb.grid(row=0, column=0, rowspan=3)
lb.bind('<<ListboxSelect>>', viewApp)

companyNameView = Label(view, text="Company: ")
companyNameView.grid(sticky = W, row=0, column=1)

jobTitleView = Label(view, padx = 5,text="Position: ")
jobTitleView.grid(sticky = W, row=0, column=2)

dateView = Label(view,padx = 5, text="Last Updated: ")
dateView.grid(sticky = W,row=1, column=1)

statusView = Label(view,padx = 5, text="Status: ")
statusView.grid(sticky = W,row=1, column=2)

platformView = Label(view,padx = 5, text="Platform: ")
platformView.grid(sticky = W,row=2, column=1)

contactView = Label(view,padx = 5, text="Contact: ")
contactView.grid(sticky = W,row=2, column=2)

lb.select_set(0)

# Run the application
window.mainloop()
appSubmission.upload_to_drive("processed_applications.csv")
