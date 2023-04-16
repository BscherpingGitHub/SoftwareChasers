# Software Chasers
# Samuel Mock

DB_HOST = "softwarec.cwmrd99bpx4t.us-east-1.rds.amazonaws.com"
DB_NAME = "Group2"
DB_user = "postgres"
DB_Pass = "null"

import psycopg2

conn = psycopg2.connect(dbname = DB_NAME, user = DB_user, password = DB_Pass, host = DB_HOST)

cur = conn.cursor()

def check_number(fname, Lname, number):
    try:
        # Insert the row into the ClientData table
        cur.execute("INSERT INTO ClientData (FirstName, LastName, SpecialNumber) VALUES (%s, %s, %s)",
                    (fname, Lname, number))
        # Commit the changes
        conn.commit()
    except UniqueViolation as e:
        # Handle the duplicate SpecialNumber error
        print("Error: A record with the same SpecialNumber already exists.")
        return -1
        conn.rollback()
    conn.commit()

    cur.close()

    conn.close()
#check_number("hans","doe",1526)
