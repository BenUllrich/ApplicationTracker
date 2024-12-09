import pytest
import pandas as pd
from Application import Application
from appSubmission import submit_application, checkCSV
from dataAnalysis import dataAnalysis
from googleSheetsAPI import connect_to_google_sheet

def test_application_creation():
    app = Application("Google", "Software Engineer", "LinkedIn", "Submitted", "John")
    assert app.getCompany() == "Google"
    assert app.getTitle() == "Software Engineer"
    assert app.getStatus() == "Submitted"
    assert app.getPlatform() == "LinkedIn"
    assert app.getConn() == "John"
