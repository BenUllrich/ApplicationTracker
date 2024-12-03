import sqlite3

conn = sqlite3.connect('applications.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS applications
             (id INTEGER PRIMARY KEY, company TEXT, position TEXT, status TEXT, date_applied TEXT)''')
