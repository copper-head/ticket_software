import sqlite3 as sq


#3. Create a python file for modifying contacts table (queries/contacts.py)
#    - Add function for creating contacts
#    - Add function for modifying contacts




def create_contact(first_name, last_name, email, phone, contact_address, connection):

    cursor = connection.cursor()

    # Query to check if the contact already is in database using EXISTS
    query = '''
        SELECT
            EXISTS (
                SELECT
                    1
                FROM
                    contacts
                WHERE
                    first_name = ?,
                    last_name = ?,
                    email = ?,
                    phone = ?,
                    contact_address = ?
            )
    '''

    # Pack data into tuple
    data = (
        first_name,
        last_name,
        email,
        phone,
        contact_address
    )

    # Execute the query
    sq.execute(query, (data,))

    # Fetch results
    results = cursor.fetchall()

    # Check if the results is empty, if empty contact doesn't exists
    if not len(results) == 0:
        return (False, "contact_exists")
    else:

        query = '''
            INSERT INTO
                contacts(
                    first_name,
                    last_name,
                    email,
                    phone,
                    contact_address
                )
            VALUES (?, ?, ?, ?, ?)
        '''

        # Insert the new contact and commit
        cursor.execute(query, (data,))
        connection.commit()


def modify_contact(first_name, last_name, email, phone, contact_address, connection):
