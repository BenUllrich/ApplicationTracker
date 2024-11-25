import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_to_google_sheet(sheet_name):
    """
    Connect to a Google Sheet using service account credentials.
    Args:
        sheet_name (str): The name of the Google Sheet.
    Returns:
        gspread.models.Worksheet: The worksheet instance.
    """
    try:
        # Define the scope
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        # Authenticate using the credentials.json file
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)

        # Debug: List all spreadsheets accessible by the service account
        print("Available Spreadsheets:")
        for spreadsheet in client.openall():
            print(f"- {spreadsheet.title}")

        # Open the specified Google Sheet
        sheet = client.open(sheet_name).sheet1
        return sheet
    except gspread.exceptions.SpreadsheetNotFound:
        raise Exception(f"Google Sheet '{sheet_name}' not found. Ensure the sheet exists and is shared with the service account.")
    except Exception as e:
        raise Exception(f"Failed to connect to Google Sheets: {e}")


def test_google_sheets_access():
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)

        # List all accessible spreadsheets
        print("Spreadsheets accessible by the service account:")
        for spreadsheet in client.openall():
            print(f"- {spreadsheet.title}")
    except Exception as e:
        print(f"Error: {e}")

def add_application_to_sheet(sheet, app):
    """
    Append application details to the Google Sheet.
    Args:
        sheet: gspread Sheet instance
        app: Instance of the Application class
    """
    try:
        # Extract data from the Application object
        data = [
            app.getCompany(),
            app.getTitle(),
            app.getStatus(),
            app.getPlatform(),
            str(app.getDate()),
            str(app.getLastUpdate()),
            app.getResume() or "Not Provided",
            app.getCoverLetter() or "Not Provided"
        ]
        sheet.append_row(data)
        # Print a success message to console or log
        print("Application successfully added to Google Sheets!")
    except Exception as e:
        # Handle errors gracefully
        print(f"Error adding application to Google Sheets: {e}")
        raise

if __name__ == "__main__":
    test_google_sheets_access()