import sqlite3 as sq
import hashlib
import secrets
import datetime
from queries.users import authenticate_user

def get_new_token(user_name, expiration_time_hrs, connection):

    cursor = connection.cursor()
    
    query = '''
        SELECT id, user_name
        FROM users
        WHERE user_name == ?
    '''

    cursor.execute(query, (user_name,))

    results = cursor.fetchall()

    if len(results) == 0:
        return (False, 'user_not_found')
    else:
    
        token = secrets.token_hex(32)
        token_salt = secrets.token_hex(16)

        hasher = hashlib.blake2s()
        hasher.update((token + token_salt).encode())
        token_hash = hasher.digest()

        st = datetime.datetime.now()
        et = st + datetime.timedelta(hours=expiration_time_hrs)

        create_time_str = f'{st.month}-{st.day}-{st.year} {st.hour}:{st.minute}:{st.second}'
        end_time_str = f'{et.month}-{et.day}-{et.year} {et.hour}:{et.minute}:{et.second}'

        data = (
            token_salt,
            token_hash,
            create_time_str,
            end_time_str,
            results[0][0]
        )

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

        connection.commit()
        return (True, token)

        


    