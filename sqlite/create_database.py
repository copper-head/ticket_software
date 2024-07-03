import sqlite3 as sq
import sys
import os

DB_FILE = "database.db"
SCHEMA_FILE = "schema.sql"

print(sys.argv)

def create_db():

    conn = sq.connect(DB_FILE)
    curs = conn.cursor()
    with open(SCHEMA_FILE, 'r') as file:
        curs.executescript(file.read())
    conn.close()

if len(sys.argv) > 1:
    if sys.argv[1].lower() == "force":
        if os.path.isfile(DB_FILE):
            in_str = input("WARNING: PROCEEDING WILL DELETE THE DATABASE AND ALL DATA WILL BE LOST! IF YOU ARE SURE, TYPE 'YES' TO CONTINUE AND PRESS ENTER. OTHERWISE THE PROCESS WILL BE ABORTED.")
            if in_str.lower() != 'yes':
                print("Aborting...")
                exit()
        create_db()
elif os.path.isfile(DB_FILE):
    print(f"{DB_FILE} file already exists. Use 'force' switch to force deletion and recreation of the database.")
else:
    create_db()

