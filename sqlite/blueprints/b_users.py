from flask import request, Blueprint
import sqlite3
import queries.users as us
from constants import *
import json

user_blueprint = Blueprint('/user/', __name__)

@user_blueprint.route('/create_user', methods=['POST'])
def create_user():

    # Put the requests dictionary in 
    rq = request.json

    # Connect to database anc create a cursor
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    # Create a new user using the create user function
    result = us.create_new_user(
        rq['username'],
        rq['password'],
        rq['first_name'],
        rq['last_name'],
        cursor
    )

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