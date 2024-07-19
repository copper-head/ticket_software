import sqlite3 as sq

#3. Create a python file for modifying contacts table (queries/contacts.py)
#    - Add function for creating contacts
#    - Add function for modifying contacts

# Description:
#       Checks to see if the contact exists
#
# Pre-Conditions:
#       contact_email (string) 
#       connections (sqlite connection object)
#
# Post:
#       returns a bool to check if the contact exists
def contact_exist(contact_email, connection):
    
    cursor = connection.cursor()

    # Query for email
    query = '''
        SELECT email
        FROM contacts
        WHERE email == ?
    '''

    # Execute the query
    cursor.execute(query, (contact_email,))

    # Fetch results of the query
    results = cursor.fetchall()

    # If there is no results, return false, else true
    if len(results) == 0:
        return False
    else:
        return True
    

    # # Query to check if the contact already is in database using EXISTS
    # query = '''
    #     SELECT
    #         EXISTS (
    #             SELECT
    #                 1
    #             FROM
    #                 contacts
    #             WHERE
    #                 first_name = ?,
    #                 last_name = ?,
    #                 email = ?,
    #                 phone = ?,
    #                 contact_address = ?
    #         )
    # '''

    # # Pack data into tuple
    # data = (
    #     first_name,
    #     last_name,
    #     email,
    #     phone,
    #     contact_address
    # )

    # # Execute the query
    # cursor.execute(query, (data,))

    # # Fetch results
    # results = cursor.fetchall()

    # # Check if the results is empty, if empty contact doesn't exists
    # if not len(results) == 0:
    #     return False
    # else:
    #     return True



def create_contact(first_name, last_name, email, phone, contact_address, connection):

    cursor = connection.cursor()

    # Check if the results is empty, if empty contact doesn't exists
    if contact_exist(email, connection):
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
        
        # Pack data into tuple
        data = (
            first_name,
            last_name,
            email,
            phone,
            contact_address
        )

        # Insert the new contact and commit
        cursor.execute(query, (data,))
        connection.commit()


def modify_contact(first_name, last_name, email, phone, contact_address, connection):
    
    # Check if the contact exists
    if not contact_exist(email, connection):
        return (False, "contact_not_found")
    else:

        cursor = connection.cursor()

        # Query to update first_name, last_name, phone, and contact_address
        query = '''
            UPDATE contacts
            SET first_name = ?,
                last_name = ?,
                phone = ?,
                contact_address = ?
            WHERE email == ?
        '''
        
        # Update and commit
        cursor.execute(query, (first_name, last_name, phone, contact_address, email,))
        connection.commit()