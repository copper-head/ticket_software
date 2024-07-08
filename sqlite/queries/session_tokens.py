import sqlite3 as sq
import hashlib
import secrets
import datetime
from queries.users import authenticate_user


def get_token_hash(token, salt):
    
    # Get the hash from salted token
    hasher = hashlib.blake2s()
    hasher.update((token + salt).encode())
    token_hash = hasher.digest()

    return token_hash


def user_exists(user_name, connection):

    cursor = connection.cursor()

    query = '''
        SELECT user_name
        FROM users
        WHERE user_name = ?
    '''

    sq.execute(query, (user_name,))
    results = cursor.fetchall()

    if len(results) == 0:
        return False
    else:
        return True



# Description:
#       Checks to see if a user_name-token pair is valid
#
# Pre-Conditions:
#       user_name (string)
#       token (string)
#       connection (sqlite connection object)
#
# Post
#
#       returns a tuple (Boolean, String)
#
def authenticate_token(user_name, token, connection):

    # Check to make sure user exists
    if not user_exists(user_name, connection):
        return (False, "user_not_found")

    cursor = connection.cursor()

    # This query returns all the needed information about tokens for
    # the specified user, if any exist.
    query = '''
        SELECT
            b.token_salt,
            b.token_hash,
            b.expiration_time
        FROM
            (
                SELECT
                    id,
                    user_name
                FROM
                    users
                WHERE
                    user_name = ?
            ) a
        JOIN
            session_tokens b
        ON
            a.id == b.user_id
    '''

    # Execute the query
    cursor.execute(query, (user_name,))

    # Fetch results of the query
    results = cursor.fetchall()

    # Loop through the results
    for value in results:

        # Get the hash for the salted token
        token_hash = get_token_hash(token, value[0])

        # If the hashes match, then make sure its not expired
        # and return result
        if token_hash == value[1]:

            exp_time = datetime.datetime.strptime(value[2], '%M-%D-%Y %H:%M:%S')
            cur_time = datetime.datetime.now()

            if exp_time > cur_time:
                return (True, "success")
            else:
                return (False, "token_expired")
    
    # If we make it here then we assume the token is invalid
    return (False, "invalid_token")


# Description:
#       Create a new token for a username. This function is a little dangerous right now
#       as there is no authentication in it. The authentication is going to be done by the API
#       But this will likely need fixed.
#
# Pre-Conditions:
#       user_name (string)
#       expiration_time_hours (float) -- Number of hours that the token will be valid for
#       conncetion (sqlite connection object) -- connection to a sqlite database
#
# Post:
#       returns a tuple (Boolean, String) which gives whether the operation
#       executed successfully and gives a short string code to infer what happened.

def get_new_token(user_name, expiration_time_hrs, connection):

    cursor = connection.cursor()
    
    query = '''
        SELECT id, user_name
        FROM users
        WHERE user_name == ?
    '''

    cursor.execute(query, (user_name,))

    results = cursor.fetchall()

    # If the user does not exist return an error
    if len(results) == 0:
        return (False, 'user_not_found')
    else:
        
        # Generate a token and a salt
        token = secrets.token_hex(32)
        token_salt = secrets.token_hex(16)

        # Get the corresponding hash for the salted token
        token_hash = get_token_hash(token, token_salt)

        # Get the current datetime and the datetime it will be in 'expiration_time_hrs' (obviously in hours)
        st = datetime.datetime.now()
        et = st + datetime.timedelta(hours=expiration_time_hrs)

        # Format the datetimes into strings for storage in the database
        create_time_str = f'{st.month}-{st.day}-{st.year} {st.hour}:{st.minute}:{st.second}'
        end_time_str = f'{et.month}-{et.day}-{et.year} {et.hour}:{et.minute}:{et.second}'

        # Pack all the data into a tuple
        data = (
            token_salt,
            token_hash,
            create_time_str,
            end_time_str,
            results[0][0]
        )

        # Cool SQL stuff
        query = '''
            INSERT INTO 
                session_tokens (
                    token_salt,
                    token_hash,
                    creation_time,
                    expiration_time,
                    user_id
                )
            VALUES
                (?, ?, ?, ?, ?)
        '''

        cursor.execute(query, data)

        # Make sure to commit those changes boys
        connection.commit()
        return (True, token)

        


    