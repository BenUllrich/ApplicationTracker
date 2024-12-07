from tkinter import *
from tkinter import  ttk

from matplotlib.pyplot import title

import Application
import appSubmission

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
       command=lambda :appSubmission.submit_application(Application.Application(company_var.get(),title_var.get(),platform_var.get(),status_var.get())))
       .grid(row=5, column=0, columnspan=2))

# Run the application
window.mainloop()
