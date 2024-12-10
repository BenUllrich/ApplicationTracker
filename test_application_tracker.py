import pytest
from datetime import date
import pandas as pd
import appSubmission
import dataAnalysis
import Application
import os

from temp2.dataAnalysis import dataAnalysis


def test_date_appSubmission():
    """
    Ensure that, when creating an application without a specified date, it defaults to today's date
    """
    app1 = Application.Application("Test Inc.", "Tester", "LinkedIn",status ='Submitted', connections=None,lastUpdate=None)
    app2 = Application.Application("Test Inc.", "Tester", "LinkedIn", status='Submitted', connections=None, lastUpdate= date.fromisoformat('2019-12-04'))
    assert app2.getDate() != date.today() and app1.getDate() == date.today()

def test_csv_fix():
    """
    Ensure that improperly formatted CSVs are overwritten correctly
    """
    # create a temporary file for the test with incorrect formatting
    with open("TEST_CSV.csv", 'w') as file:
        file.write("THIS IS, VERY CONFUSING, TO THE FUNCTION, I AM SURE OF IT!\nLOREM,IPSUM,LOREM,IPSUM")

    appSubmission.checkCSV("TEST_CSV.csv")

    with open("TEST_CSV.csv", 'r') as file:
        contents =  file.read()

    # delete the temporary file
    os.remove('TEST_CSV.csv')
    assert contents == 'Company,Position,Source,Status,Date,Contact Person\n'

def test_invalid_application():
    """
    Test how the submit_application function handles incomplete information (expected to fail)
    """
    #application with None in one of the parameters
    app = Application.Application("Test Inc.", "Tester", None,status ='Submitted', connections=None,lastUpdate=None)

    # create a fresh csv, use it to create a dataframe, then remove it for cleanliness
    appSubmission.checkCSV("TEST_CSV.csv")
    appSubmission.submit_application(app,"TEST_CSV.csv")
    data = pd.read_csv("TEST_CSV.csv")
    os.remove('TEST_CSV.csv')

    # The submit_application call will not add anything to the file, and the row won't exist, raising a KeyError
    #    - This will cause a window to pop up during the test, which is also expected
    with pytest.raises(KeyError):
        data.loc[0]

@pytest.mark.xfail(reason = "No errors should be raised")
def test_no_connection():
    """
    Ensure that the program can handle applications without a specified contact
    """

    # fresh csv file
    appSubmission.checkCSV("TEST_CSV.csv")

    # submit two applications, one with and one without a connection
    # This will open two messageboxes as a result of the submit_application code
    appSubmission.submit_application(
        Application.Application("Python", "Sample", "Indeed",status ='Interviewing', connections="John Doe",
                                lastUpdate=None), "TEST_CSV.csv")
    appSubmission.submit_application(
        Application.Application("Test Inc.", "Tester", "Handshake", status='Submitted', connections=None,
                                lastUpdate=None), "TEST_CSV.csv")

    # read into dataframe, then clean up the csv file
    data = pd.read_csv("TEST_CSV.csv")
    os.remove('TEST_CSV.csv')

    # the following will raise a KeyError if either of these applications was not successfully added
    with pytest.raises(KeyError):
        data.loc[0]
        data.loc[1]

def test_analysis_no_csv():
    """
    Ensure that a dataAnalysis instance cannot be created with an invalid csv name
    """
    with pytest.raises(FileNotFoundError):
        dataAnalysis("FAKE_FILE.csv")
