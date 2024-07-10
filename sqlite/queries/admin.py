import sqlite as sq


def query_users(keyword, condition, connection):
    
    if condition == "starts_with":
        
        query = '''
            SELECT
                user_name,
                first_name,
                last_name,
                is_admin
            FROM
                users
            WHERE user_name ==
        '''

    elif condition == "contains":
        pass
    elif condition == "exactly":
        pass
    elif condition == "all":
        pass
    else:
        pass