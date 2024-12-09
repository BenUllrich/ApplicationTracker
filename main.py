from tkinter import *
from tkinter import ttk

import Application
import appSubmission
import pandas as pd
from dataAnalysis import dataAnalysis

def updateApp(event):
    """
    Updates the entry boxes depending on the selected application in the update tab
    :param event:
    :return:
    """
    if lbUpdate.curselection():
        updateEntry.delete(0, END)
        # only include contact if contact exists:
        if not pd.isna(apps.loc[lbUpdate.curselection()[0], 'Contact Person']):
            updateEntry.insert(0, apps.loc[lbUpdate.curselection()[0], 'Contact Person'])
        # unlike contact, status always exists:
        editStatus_var.set(apps.loc[lbUpdate.curselection()[0], 'Status'])


def refresh(arg=None):
    """
    Refreshes the listboxes throughout the interface
    :param arg: The type of change that was made (newapp or update)
    :return:
    """
    global apps
    global analytics
    if arg == 'newapp':
        # clear listboxes:
        lb.delete(0, END)
        lbUpdate.delete(0,END)

        # create and submit the new app using UI input
        appSubmission.submit_application(
            Application.Application(company_var.get(), title_var.get(), platform_var.get(), status_var.get(),
                                    conn_var.get())
        )

        # re-read the csv after submitting applications, then update the listboxes with the new csv info
        apps = pd.read_csv("processed_applications.csv")
        for index, row in apps.iterrows():
            lb.insert(index, f"{row['Company']:}  ({row['Date']:>})")
            lbUpdate.insert(index, f"{row['Company']:}  ({row['Date']:>})")

    if arg == 'update':
        # make sure an application is selected before trying to update it
        if lbUpdate.curselection():
            index = lbUpdate.curselection()[0]

            # Create a new application, updating only the fields the user actually inputs
            if editStatus_var.get() and editConn_var.get().strip():
                new = Application.Application(apps.loc[index, 'Company'], apps.loc[index, 'Position'], apps.loc[index, 'Source'], editStatus_var.get(),
                                        editConn_var.get())
            elif editStatus_var.get():
                new = Application.Application(apps.loc[index, 'Company'], apps.loc[index, 'Position'],
                                              apps.loc[index, 'Source'], editStatus_var.get(),
                                              apps.loc[index, 'Contact Person'])
            elif editConn_var.get().strip():
                new = Application.Application(apps.loc[index, 'Company'], apps.loc[index, 'Position'],
                                              apps.loc[index, 'Source'], apps.loc[index, 'Status'],
                                              editConn_var.get())
            else: return

            # Remove the old application and re-create the local CSV
            apps.drop(index, inplace = True)
            apps.to_csv("processed_applications.csv", index = False)

            # Clear listboxes
            lb.delete(0, END)
            lbUpdate.delete(0, END)

            # Submit the updated application, update listboxes
            appSubmission.submit_application(new)
            apps = pd.read_csv("processed_applications.csv")
            for i, row in apps.iterrows():
                lb.insert(i, f"{row['Company']:}  ({row['Date']:>})")
                lbUpdate.insert(i, f"{row['Company']:}  ({row['Date']:>})")

    analytics = dataAnalysis("processed_applications.csv")


def viewApp(event):
    """
    Updates the information fields when a new application is selected in the view tab
    :param event:
    :return:
    """
    if lb.curselection():

           # Update all UI elements:
           companyNameView.config(text="Company: " + apps.loc[lb.curselection()[0], 'Company'])
           jobTitleView.config(text="Position: " + apps.loc[lb.curselection()[0], 'Position'])
           dateView.config(text="Last Updated: " + apps.loc[lb.curselection()[0], 'Date'])
           statusView.config(text="Status: " + apps.loc[lb.curselection()[0], 'Status'])
           platformView.config(text="Platform: " + apps.loc[lb.curselection()[0], 'Source'])

           # Use the isna() function to test if contact person is present (nan isn't a falsy somehow)
           # Required so that you don't get an error message for trying to add nan to string
           if pd.isna(apps.loc[lb.curselection()[0], 'Contact Person']):
               contactView.config(text="Contact: ")
           else:
               contactView.config(text="Contact: " + str(apps.loc[lb.curselection()[0], 'Contact Person']))


# TODO: CREATE + ADD CODE TO CONNECT GOOGLE DRIVE BEFORE UI OPENS

# check for csv, then create an object for data analysis
appSubmission.checkCSV("processed_applications.csv")
analytics = dataAnalysis("processed_applications.csv")

# Set up the window
window = Tk()
window.title("Application Tracker")
window.resizable(width=False, height=False)

# A notebook is used to organize the functionality
tabs = ttk.Notebook(window)
tabs.pack(expand=1)

# Notebook tabs:
view = ttk.Frame(tabs)
tabs.add(view, text="View Applications")
add = ttk.Frame(tabs)
tabs.add(add, text="Add New Application")
edit = ttk.Frame(tabs)
tabs.add(edit, text="Update Applications")
analysis = ttk.Frame(tabs)
tabs.add(analysis, text="View Analysis")

# ADDING APPLICATIONS
# ---------------------------------------------------------------------------------
Label(add, text="Company").grid(row=0, column=1,pady=10)
company_var = StringVar()
Entry(add, textvariable=company_var).grid(row=0, column=2,pady=10)

Label(add, text="Job Title").grid(row=1, column=1,pady=10)
title_var = StringVar()
Entry(add, textvariable=title_var).grid(row=1, column=2,pady=10)

Label(add, text="App Platform").grid(row=2, column=1,pady=10)
platform_var = StringVar()
Entry(add, textvariable=platform_var).grid(row=2, column=2, pady=10)

Label(add, text="Application Status").grid(row=3, column=1, padx = 4)
status_var = StringVar()
status_var.set("Options")
options = OptionMenu(add, status_var, "Submitted", "Interviewing", "Offer Received", "Rejected")
options.config(width = 12)
options.grid(row=3, column=2,pady=10)

Label(add, text="Connections").grid(row=4, column=1,pady=10)
conn_var = StringVar()
Entry(add, textvariable=conn_var).grid(row=4, column=2,pady=10)
Button(add, text="Submit", padx = 15,
        # run the refresh function to create the new application
        command=lambda: refresh('newapp')).grid(row=5, column=1, columnspan=2,pady=10)

# VIEWING APPLICATIONS:
# ---------------------------------------------------------------------------------

# populate from dataframe
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


# UPDATE APPLICATIONS
# ---------------------------------------------------------------------------------
lbUpdate = Listbox(edit, width= 30, height = 15)
apps = pd.read_csv("processed_applications.csv")
for index, row in apps.iterrows():
    lbUpdate.insert(index, f"{row['Company']:}  ({row['Date']:>})")

Label(edit, text="New Connection:").grid(row=0, column=1)
editConn_var = StringVar()

updateEntry = Entry(edit, textvariable=editConn_var)
updateEntry.grid(row=0, column=2)

Label(edit, text="Update Application Status").grid(row=1, column=1)
editStatus_var = StringVar()
status_var.set("Options")
OptionMenu(edit, editStatus_var, "Submitted", "Interviewing", "Offer Received", "Rejected").grid(row=1, column=2)

lbUpdate.grid(row=0, column=0, rowspan=3)
lbUpdate.bind('<<ListboxSelect>>', updateApp)
Button(edit, text="Update",
        command=lambda: refresh('update')).grid(row=5, column=0, columnspan=3)

lbUpdate.select_set(0)

# DATA ANALYSIS
# ---------------------------------------------------------------------------------
Button(analysis, text="Applications by Status",height=3, width=20,
       command=lambda: analytics.show_status_counts()
       ).grid(row = 1, column =1, padx = (100,5), pady =5)
Button(analysis, text="Applications by Source",height=3, width=20,
       command=lambda: analytics.show_source_counts()
       ).grid(row = 1, column =2, padx = (5,100), pady =5)
Button(analysis, text="Applications by Company",height=3, width=20,
       command=lambda: analytics.show_company_counts()
       ).grid(row = 2, column =1, padx = (100,5), pady =5)
Button(analysis, text="Applications Timeline",height=3, width=20,
       command=lambda: analytics.show_timeline()
       ).grid(row = 2, column =2, padx = (5,100), pady =5)
Button(analysis, text="Application\nStatus + Source",height=3, width=20,
       command=lambda: analytics.show_status_source()
       ).grid(row = 3, column =1, columnspan=2, pady =5)

# Run the application
window.mainloop()

# when UI is closed, attempt to upload csv to drive
appSubmission.upload_to_drive("processed_applications.csv")
