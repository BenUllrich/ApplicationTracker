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
- Using the Google Sheets API, the app will open an existing spreadsheet (or create a new one if it does not yet exist)
- Each row in this sheet will store an instance of the Application Object
  - This object will be used to store information about each individual application, as well as handle tasks such as adding information, updating the status, deleting the application, etc.
- The user will be able to view, edit, and create new applications, which will be added to the active pandas dataframe, then uploaded to Google Drive
- We can try an autosave feature, but for now, we should focus on a "Save" button to update the spreadsheet

## Login page

## Welcome Page
- Welcome Message
- Job application analytics - Graphical representation of the application status

## Applications Page
- Table list of all applications - Job Title | Company | Applied Date | Status | Connections | Notes/Reminders
- Status update button or set a reminder
  - new connection
  - to prep for interview
  - send an email
  - follow up
    

## Company Directory Page
- Table View of the Companies shortlisted - Company | Industry | Locations | Connections | Notes/Reminders
- Status update button
  - New connections made
- Set a reminder - to events / check  for new job openings / follow up with the network 

