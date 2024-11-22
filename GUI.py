import tkinter as tk

def applicationsMenu():
    return

def settingsMenu():
    return

def filesMenu():
    return

def mainMenu():
    # Set up the window
    window = tk.Tk()
    window.title("Main Menu")
    window.resizable(width=False, height=False)
    window.size()


    btn_apps = tk.Button(
        master=window,
        text="Applications",
        command=applicationsMenu(),
        width=20,
        height=5
    )
    btn_settings = tk.Button(
        master=window,
        text="Settings",
        command=applicationsMenu(),
        width=20,
        height=5
    )
    btn_files = tk.Button(
        master=window,
        text="Files",
        command=applicationsMenu(),
        width=20,
        height=5
    )

    # Set up the layout using the .grid() geometry manager
    btn_apps.grid(row=0, column=1, pady=10, padx = 15)
    btn_files.grid(row=1, column=1, pady=10, padx = 15)
    btn_settings.grid(row=2, column=1, pady=10, padx = 15)


    # Run the application
    window.mainloop()
