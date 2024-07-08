from flask import request, Blueprint
import sqlite3
import queries.users as us
import queries.session_tokens as st
from constants import *
import json

user_blueprint = Blueprint('/user/', __name__)


@user_blueprint.route('/user/create_user', methods=['POST'])
def create_user():

    # Put the requests dictionary in 
    rq = request.json

    # Connect to database anc create a cursor
    connection = sqlite3.connect(DB_FILE)

    # Create a new user using the create user function
    result = us.create_new_user(
        rq['username'],
        rq['password'],
        rq['first_name'],
        rq['last_name'],
        connection
    )

    connection.close()

    # Handle the result of the account creation function
    if result[0] == True:
        ret_dict = {'TYPE': 'success', 'MESSAGE': "Account created successfully"}
        return json.dumps(ret_dict)
    elif result[1] == 'account_exists':
        ret_dict = {'TYPE': 'error', 'MESSAGE': "Account already exists"}
        return json.dumps(ret_dict)
    else:
        ret_dict = {'TYPE': 'error', 'MESSAGE': "Server error occurred"}
        return json.dumps(ret_dict)
    

@user_blueprint.route('/user/get_token', methods=['GET'])
def get_user_token():
    
    rq = request.json

    connection = sqlite3.connect(DB_FILE)

    result = st.get_new_token(
        rq['user_name'],
        rq['time_in_hours'],
        connection
    )

    if result[0] == True:
        ret_dict = {
            'TYPE': 'success', 
            'MESSAGE': 'Token created successfully', 
            'TOKEN': result[1]
        }
    elif result[1] == 'user_not_found':
        ret_dict = {
            'TYPE': 'error', 
            'MESSAGE': f'Could not find user {rq['user_name']}'
        }
    else:
        ret_dict = {
            'TYPE': 'error', 
            'MESSAGE': 'Server error occurred'
        }
    
    connection.close()
    return json.dumps(ret_dict)


@user_blueprint.route('/admin/get_users', methods=['GET'])