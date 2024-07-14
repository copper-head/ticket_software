import sqlite
import datetime
import contacts as co

# TO DO:
#    - Create a function for deleting tickets - Note that we will need to CASCADE
#    as there will be log entries that must be deleted to maintain referential
#    integrity (might be best to leave this till later for now)

# Description:
#       Creates a ticket
#
# Pre-Conditions:
#       contact_email (string)
#       issue_title (string)
#       connection (sqlite connection object)
#
# Post:
#       inserts a ticket into the database
def create_ticket(contact_email, issue_title, connection):

    # Checks to see if the contact exists
    if not co.contact_exist(contact_email, connection):
        return (False, "contact_not_found")
    else:

        cursor = connection.cursor()

        # Query to fetch contact_id
        query = '''
            SELECT contact_id
            FROM contacts
            WHERE contact_id == ?
        '''

        # Execute the query
        cursor.execute(cursor, (query,))

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
                tickets(
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

# Description:
#       Modifys a tickets attributes
#
# Pre-Conditions:
#       contact_email (string)
#       issue_title (string)
#       connections (sqlite connection object)
#
# Post:
#       Updates a tickets attributes
def modify_ticket(contact_email, issue_title, connection):

    # Checks to see if the contact exists
    if not co.contact_exist(contact_email, connection):
        return (False, "contact_not_found")
    else:

        cursor = connection.cursor()

        # This query only updates the ticket's issue_title
        # MUST HAVE WHERE!!! Otherwise UPDATE will modify all rows in the table
        query = '''
            UPDATE tickets
            SET issue_title = ?
            WHERE contact_email = ?
        '''

        # Put data into a tuple
        data = (
            issue_title,
            contact_email
        )

        # Update and commit
        cursor.execute(query, data)
        connection.commit()

# Description:
#       Checks to see if a ticket exists in the database
#
# Pre-Conditions:
#       ticket_id (integer)
#       connection (sqlite connection object)
#
# Post:
#       Returns true if the ticket exists
def ticket_exists(ticket_id, connection):

    cursor = connection.cursor()
    
    # Query to see if ticket exists
    query = '''
        SELECT id
        FROM tickets
        WHERE id = ?
    '''

    # Execute the query
    cursor.execute(query, (ticket_id,))

    # Fetch the results of the query
    results = cursor.fetchall()

    # Return true if there are any results, false otherwise
    return len(results) > 0
