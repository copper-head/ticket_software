import sqlite3 as sq
import datetime
import tickets as ti


# Description:
#       Creates a log atatched to a ticket in the database
#
# Pre-Conditions:
#       body_text (string)
#       logs_type (string)
#       ticket_id (integer)
#       connection (sqlite connection object)
#
# Post:
#       Inserts a log into the database that should be attached to a ticket
def create_log(body_text, logs_type, ticket_id, connection):

    # Check to see if ticket exists
    if not ti.ticket_exists(ticket_id, connection):
        return (False, "ticket_not_found")
    else:
        
        cursor = connection.cursor()

        # Get the current datetime
        st = datetime.datetime.now()
        
        # Format the datetimes into strings for storage in the database
        time_stamp = f'{st.month}-{st.day}-{st.year} {st.hour}:{st.minute}:{st.second}'


        # Put data into a tuple
        data = (
            time_stamp,
            body_text,
            logs_type,
            ticket_id
        )

        # Query to create the ticket
        query = '''
            INSERT INTO
                logs(
                    time_stamp,
                    body_text,
                    logs_type,
                    ticket_id
                )
            VALUES
                (?, ?, ?, ?)
        '''

        # Execute the query and commit the changes
        cursor.execute(query, (data,))
        connection.commit()
        return(True)


# Description:
#       Checks if the ticket already exists in the database
#
# Pre-Conditions:
#       body_text (string)
#       logs_type (string)
#       ticket_id (integer)
#       connection (sqlite connection object)
#
# Post:
#       Returns true if the ticket already exists in the database
def log_exists(body_text, logs_type, ticket_id, connection):
    
    cursor = connection.cursor()

    # Query to see if log exists
    query = '''
        SELECT
            body_text,
            logs_type,
            ticket_id
        FROM logs
        WHERE
            body_text = ?
            AND logs_type = ?
            AND ticket_id = ?
    '''

    # Put data into a tuple
    data = (
        body_text,
        logs_type,
        ticket_id
    )

    # Execute the query
    cursor.execute(query, data)

    # Fetch the results
    results = cursor.fetchall()

    # Return true if there are any results, false otherwise
    return len(results) > 0