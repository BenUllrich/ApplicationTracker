# Author: Benjamin Ullrich, Dhavan Antala, Om Gaikwad
# Date: December 10, 2024
# Description: A class that uses matplotlib to display application information

import pandas as pd
import matplotlib.pyplot as plt
import os
from tkinter import messagebox

class dataAnalysis:
    def __init__(self,csvName):
        if not os.path.exists(csvName):
            raise FileNotFoundError
        try:
            self.__applications = pd.read_csv(csvName)
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return
        if 'Status' not in self.__applications.columns:
            messagebox.showerror("Error", "'Status' column is missing in the data.")
            return
        elif 'Date' in self.__applications.columns:
            self.__applications['Date'] = pd.to_datetime(self.__applications['Date'], errors='coerce')  # Convert to datetime, handling errors
        else:
            messagebox.showerror("Error", "Dates Missing from .CSV file")

        # the following variables will be used to display graphs and charts:

        self.__status_counts = self.__applications['Status'].value_counts()
        self.__source_counts = self.__applications['Source'].value_counts()
        self.__applications_timeline = self.__applications['Date'].value_counts().sort_index()
        self.__grouped = self.__applications.groupby(['Status', 'Source']).size().unstack()
        self.__company_counts = self.__applications['Company'].value_counts()

    def show_status_counts(self):
        """
        Display a bar chart of application status counts.
        """
        try:
            plt.figure(figsize=(8, 6))
            self.__status_counts.plot(kind='bar', color='skyblue')
            plt.title("Application Status Count")
            plt.xlabel("Status")
            plt.ylabel("Number of Applications")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except:
            messagebox.showerror("Error", "Data Missing!")

    def show_timeline(self):
        """
        Display a chart showing the updates per date for applications
        """
        try:
            plt.figure(figsize=(10, 6))
            self.__applications_timeline.plot(kind='line', marker='o')
            plt.title("Applications Over Time")
            plt.xlabel("Date")
            plt.ylabel("Number of Applications")
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except:
            messagebox.showerror("Error", "Data Missing!")

    def show_source_counts(self):
        """
        Display a chart showing the applications for each source
        """
        try:
            plt.figure(figsize=(8, 6))
            self.__source_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
            plt.title("Applications by Source")
            plt.ylabel("")  # Hide y-label for a cleaner look
            plt.tight_layout()
            plt.show()
        except:
            messagebox.showerror("Error", "Data Missing!")

    def show_status_source(self):
        """
        Display a chart showing the applications in each status
        """
        try:
            self.__grouped.plot(kind='bar', figsize=(12, 8))
            plt.title("Applications Grouped by Status and Source")
            plt.xlabel("Status")
            plt.ylabel("Number of Applications")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except:
            messagebox.showerror("Error", "Data Missing!")

    def show_company_counts(self):
        """
        Display a chart showing the number of applications for each company
        """
        try:
            self.__company_counts.plot(kind='bar', figsize=(12, 8), color='skyblue')
            plt.title("Applications by Company")
            plt.xlabel("Company")
            plt.ylabel("Number of Applications")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except:
            messagebox.showerror("Error", "Data Missing!")
