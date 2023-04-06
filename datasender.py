# Software Chasers
# Samuel Mock

DB_HOST = "softwarec.cwmrd99bpx4t.us-east-1.rds.amazonaws.com"
DB_NAME = "Group2"
DB_user = "postgres"
DB_Pass = "Computer"

import psycopg2
from psycopg2.errors import UniqueViolation

conn = psycopg2.connect(dbname = DB_NAME, user = DB_user, password = DB_Pass, host = DB_HOST)

cur = conn.cursor()

#cur.execute("""
#CREATE TABLE ClientData (
#    id SERIAL PRIMARY KEY,
#    FirstName VARCHAR(16) NOT NULL,
#    LastName VARCHAR(16) NOT NULL,
#    SpecialNumber BIGINT UNIQUE
#);
#""")
#cur.execute("INSERT INTO ClientData (FirstName, LastName, SpecialNumber) VALUES (%s, %s, %s)", ("John", "Doe", 777))
try:
    # Insert the row into the ClientData table
    cur.execute("INSERT INTO ClientData (FirstName, LastName, SpecialNumber) VALUES (%s, %s, %s)", ("John", "Doe", 777))
    # Commit the changes
    conn.commit()
except UniqueViolation as e:
    # Handle the duplicate SpecialNumber error
    print("Error: A record with the same SpecialNumber already exists.")
    conn.rollback()
conn.commit()

cur.close()

conn.close()