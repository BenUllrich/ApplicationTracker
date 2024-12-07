import pandas as pd
import matplotlib.pyplot as plt

# Sample data (Replace this with reading from your file if needed)
data = {
    'Company': ['Google', 'Amazon', 'Google', 'NVIDIA', 'Tesla', 'Meta', 'Goldman Sachs',
                'Morgan Stanley', 'Citadel', 'JP Morgan'],
    'Position': ['Software Engineer', 'Robotics Engineer', 'Software Engineer', 'Hardware Engineer',
                 'Battery Engineer', 'Application Engineer', 'Quant Analyst',
                 'Risk Analyst', 'Quant Researcher', 'Software Engineer'],
    'Source': ['LinkedIn', 'LinkedIn', 'Handshake', 'LinkedIn', 'LinkedIn', 'Indeed', 'LinkedIn',
               'Handshake', 'Indeed', 'Handshake'],
    'Status': ['Interviewing', 'Interviewing', 'Submitted', 'Rejected', 'Offer Received',
               'Submitted', 'Offer Received', 'Rejected', 'Submitted', 'Offer Received'],
    'Date': ['12/6/2024', '12/7/2024', '12/7/2024', '12/7/2024', '12/7/2024',
             '12/7/2024', '12/7/2024', '12/7/2024', '12/7/2024', '12/7/2024'],
    'Contact Person': ['Om Gaikwad', 'Ben', 'Om', 'John', 'Mike', 'Rob', 'Sam', 'Dhavan', 'Matt', 'Joe']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Example analysis and visualizations
# -----------------------------------

# 1. Count of applications by status
status_counts = df['Status'].value_counts()
plt.figure(figsize=(8, 6))
status_counts.plot(kind='bar')
plt.title('Application Status Count')
plt.xlabel('Status')
plt.ylabel('Number of Applications')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Applications by Source
source_counts = df['Source'].value_counts()
plt.figure(figsize=(8, 6))
source_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Applications by Source')
plt.ylabel('')  # Hide the y-label for better appearance
plt.tight_layout()
plt.show()

# 3. Applications by Company
company_counts = df['Company'].value_counts()
plt.figure(figsize=(10, 6))
company_counts.plot(kind='barh', color='skyblue')
plt.title('Applications by Company')
plt.xlabel('Number of Applications')
plt.ylabel('Company')
plt.tight_layout()
plt.show()

# 4. Applications timeline
applications_timeline = df['Date'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
applications_timeline.plot(kind='line', marker='o')
plt.title('Applications Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Applications')
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Applications grouped by Status and Source
grouped = df.groupby(['Status', 'Source']).size().unstack()
grouped.plot(kind='bar', figsize=(12, 8))
plt.title('Applications Grouped by Status and Source')
plt.xlabel('Status')
plt.ylabel('Number of Applications')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Additional methods of exploration:
# ----------------------------------

# a. Summary statistics
print(df.describe(include='all'))

# b. Applications by Contact Person
contact_counts = df['Contact Person'].value_counts()
print(contact_counts)

# c. Exporting the processed data to a file
df.to_csv('processed_applications.csv', index=False)
