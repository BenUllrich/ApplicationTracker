# Application Tracker
## Ben Ullrich, Dhavan Antala, and Om Gaikwad

To Do List:
- [ ] UI
  - [ ] Applications Menu
    - [ ] List applications from csv/google sheets file (pandas)
    - [ ] Update/edit applications (pandas)
- [ ] Google drive API functionality
  - [ ] Read CSV into pandas
  - [ ] create new CSV if file doesn't exist
- [ ] Testing

## Functionality Description:
- On launch, You will be prompted to sign in to Google Drive
- Using the Google Sheets API, the app will download the existing spreadsheet from drive
  - If not found, a blank local csv will be created
- Each row in this sheet will store an instance of the Application Object
  - This object will be used to store information about each individual application, as well as handle tasks such as adding information, updating the status, deleting the application, etc.
- The user will be able to view, edit, and create new applications, which will be added to the active pandas dataframe, then uploaded to Google Drive when the UI is closed
  - The user will be notified if this is not successful. No data will be lost from the existing file

# Dependencies:


# UI Layout
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

