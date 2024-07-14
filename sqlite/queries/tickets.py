import sqlite as sq
import datetime


#1. Create python file for modifying tickets table (queries/tickets.py)
#    - Add function for creating tickets.
#    - Add function for modifying ticket attributes
#    - Create a function for deleting tickets - Note that we will need to CASCADE
#    as there will be log entries that must be deleted to maintain referential
#    integrity (might be best to leave this till later for now)


# Description:
#       Checks to see if the contact for the ticket exist
#
# Pre-Conditions:
#       contact_email (string) 
#       connections (sqlite connection object)
#
# Post:
#       returns a bool to check if the contact exists
def contact_exist(contact_email, connection):
    
    cursor = connection.cursor()

    # checking for id but could change schema to make contacts email unique
    #query = '''
    #    SELECT id
    #    FROM contacts
    #    WHERE id == ?
    #'''
    # possible query for email
    query = '''
        SELECT email
        FROM contacts
        WHERE email == ?
    '''

    # Execute the query
    sq.execute(query, (contact_email,))

    # Fetch results of the query
    results = cursor.fetchall()

    # If there is no results, return false, else true
    if len(results) == 0:
        return False
    else:
        return True
    


def create_ticket(contact_email, issue_title, connection):

    # Checks to see if the contact exists
    if not contact_exist(contact_email, connection):
        return (False, "contact_not_found")
    else:

        # Fetch contact id
        cursor = connection.cursor()

        query = '''
            SELECT contact_id
            FROM contacts
            WHERE contact_id == ?
        '''

        # Execute the query
        sq.execute(cursor, (query,))

        # Fetch results of the query
        results = cursor.fetchall()
        
        # If there is no results, return false
        if len(results) == 0:
            return (False, "contact_not_found")
        else:
            contact_id = results
        
        # Get the current datetime
        st = datetime.datetime.now()
        
        # Format the datetimes into strings for storage in the database
        create_time_str = f'{st.month}-{st.day}-{st.year} {st.hour}:{st.minute}:{st.second}'

        # Pack data into tuple
        data = (
            create_time_str,
            issue_title,
            contact_id
        )

        query = '''
            INSERT INTO
                tickets (
                    open_date,
                    issue_title,
                    contact_id
                )
            VALUES
                (?, ?, ?)
        '''

        # Execute the query
        cursor.execute(query, data)

        # Commits the changes
        connection.commit()
        return (True)


def modify_ticket(contact_email, new_issue_title, connection):

    # Checks to see if the contact exists
    if not contact_exist(contact_email, connection):
        return (False, "contact_not_found")
    else:

        cursor = connection.cursor()

        # This query only updates the ticket's issue_title
        # MUST HAVE WHERE!!! Otherwise UPDATE will modify all rows in the table
        query = '''
            UPDATE contacts
            SET issue_title = ?
            WHERE contact_email = ?
        '''

        # Update and commit
        cursor.execute(query, (new_issue_title, contact_email,))
        connection.commit()