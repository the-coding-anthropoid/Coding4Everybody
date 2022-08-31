"""
Task:
    Write an application that will read the mailbox data (mbox.txt) and count 
    the number of email messages per organization (i.e. domain name of the email 
    address) and use a database with the following schema to maintain the counts.

    '''CREATE TABLE Counts (org TEXT, count INTEGER)'''

Version:
    0.2.2
"""

import sqlite3

# connect to database
conn = sqlite3.connect('autograder-count-mail.sqlite')
cur = conn.cursor()
# delete table 'Counts' if it already exists
cur.execute('DROP TABLE IF EXISTS Counts')
# create table 'Counts' with two fields > 'org' and 'count'
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# open file
fhand = open("mbox.txt")

# iterate file
for line in fhand:
    # get "From " lines
    if line.startswith("From "):
        # get domain from line
        org = line.split()[1].split('@')[1]
        # look-up domain
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
        # if not in table, insert
        if row is None:
            cur.execute('''
                INSERT INTO Counts (org, count) VALUES (?, 1)''', 
                (org,))
        # if in table, update count
        else:
            cur.execute('''
                UPDATE Counts SET count = count + 1 WHERE org = ?''', 
                (org,))

# save database
conn.commit()

# close database
cur.close()