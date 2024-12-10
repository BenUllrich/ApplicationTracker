import pytest
import os
from dataAnalysis import dataAnalysis

# Define the path to the CSV file
CSV_FILE = "applications.csv"

# Create test cases for the `dataAnalysis` class
@pytest.fixture
def analysis_instance():
    """
    Fixture to create an instance of the `dataAnalysis` class.
    """
    return dataAnalysis(CSV_FILE)

def test_file_exists():
    """
    Test if the CSV file exists in the correct directory.
    """
    assert os.path.exists(CSV_FILE), f"CSV file '{CSV_FILE}' does not exist."

def test_data_loading(analysis_instance):
    """
    Test if the data is loaded correctly into the `dataAnalysis` instance.
    """
    assert not analysis_instance._dataAnalysis__applications.empty, "Data was not loaded correctly."

def test_status_counts(analysis_instance):
    """
    Test if the status counts are calculated correctly.
    """
    status_counts = analysis_instance._dataAnalysis__applications['Status'].value_counts()
    assert len(status_counts) > 0, "Status counts are empty."

def test_timeline_graph(analysis_instance):
    """
    Test if the timeline graph can be generated without errors.
    """
    try:
        analysis_instance.show_timeline()
    except Exception as e:
        pytest.fail(f"Timeline graph failed to generate: {e}")

def test_source_counts_graph(analysis_instance):
    """
    Test if the source counts graph can be generated without errors.
    """
    try:
        analysis_instance.show_source_counts()
    except Exception as e:
        pytest.fail(f"Source counts graph failed to generate: {e}")

def test_status_source_graph(analysis_instance):
    """
    Test if the status and source grouped graph can be generated without errors.
    """
    try:
        analysis_instance.show_status_source()
    except Exception as e:
        pytest.fail(f"Status source graph failed to generate: {e}")

def test_company_graph(analysis_instance):
    """
    Test if the applications by company graph can be generated without errors.
    """
    try:
        analysis_instance.show_company_graph()
    except Exception as e:
        pytest.fail(f"Applications by company graph failed to generate: {e}")
