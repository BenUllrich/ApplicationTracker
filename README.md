# Application Tracker
### Ben Ullrich, Dhavan Antala, and Om Gaikwad

## Dependencies:
- pandas
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client
- matplotlib

## To Run:
> git clone https://github.com/BenUllrich/ApplicationTracker
#### In Directory ApplicationTracker:
> Python main.py

## Functionality Description:
- On launch, user will be prompted to sign in to Google Drive
- Using the Google Drive API, the app will download the existing spreadsheet from the user's drive
  - If not found, a blank local csv will be created
- Each row in this sheet will store an instance of the Application Object
  - This object will be used to store information about each individual application, as well as handle tasks such as adding information, updating the status, deleting the application, etc.
- The user will be able to view, edit, and create new applications, which will be added to the active pandas dataframe, then uploaded to Google Drive when the UI is closed
  - The user will be notified if this is not successful.

## UI Layout
### View Applications
- Table list of all applications
   - Select to view Job Title | Company | Last Update | Status | Connections

### Add New Application
 - Accepts user input for all fields
    - Adding a connection is optional

### Update Applications
- Status update menu
- Change connection
- Delete application 

### Data Analytics
- Job application analytics - Graphical representation of the application status
  - Applications by status
  - Applications by source
  - Applications by company
  - Applications timeline
  - Application status + source

