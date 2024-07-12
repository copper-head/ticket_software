#include<iostream>
#include<string>
using namespace std;


//Global variables
string token;
bool is_valid = false;

// the grammer is ([attribute] [conditional] [data_type]) ([logical_op] [attribute] [condtional] [data_type])

void get_token()
{
    cin >> token;
    return;
}


// not completly sure what an attribute is? is it a string? int?
bool is_attribute(string token)
{
    bool temp = false;
    
    // users attributes
    if (token == "id")
        temp = true;
    else if(token == "user_name")
        temp = true;
    else if(token == "password_salt")
        temp = true;
    else if(token == "password_hash")
        temp = true;
    else if(token == "first_name")
        temp = true;
    else if(token == "last_name")
        temp = true;
    else if(token == "is_admin")
        temp = true;
    
    // session_tokens attributes
    if (token == "id")
        temp = true;
    else if(token == "token_salt")
        temp = true;
    else if(token == "token_hash")
        temp = true;
    else if(token == "creation_time")
        temp = true;
    else if(token == "expiration_time")
        temp = true;
    else if(token == "user_id")
        temp = true;
    
    // tickets attributes
    if (token == "id")
        temp = true;
    else if(token == "open_date")
        temp = true;
    else if(token == "close_date")
        temp = true;
    else if(token == "issue_title")
        temp = true;
    else if(token == "contact_id")
        temp = true;
    
    // logs attributes
    if (token == "id")
        temp = true;
    else if(token == "time_stamp")
        temp = true;
    else if(token == "body_text")
        temp = true;
    else if(token == "logs_type")
        temp = true;
    else if(token == "ticket_id")
        temp = true;
    
    // contacts attributes
    if (token == "id")
        temp = true;
    else if(token == "first_name")
        temp = true;
    else if(token == "last_name")
        temp = true;
    else if(token == "email")
        temp = true;
    else if(token == "phone")
        temp = true;
    else if(token == "contact_address")
        temp = true;
    else if(token == "is_a_massive_piece_of_shit")
        temp = true;

    return temp;
}


bool is_comparison(string token)
{
    // comparison operators includes "=", "==", "<", "<=", ">", ">=", "!=", "", "IN", "NOT IN", "BETWEEN", "IS", and "IS NOT"
    bool temp = false;

    if(token == "=")
        temp = true;
    else if (token == "==")
        temp = true;
    else if (token == "<")
        temp = true;
    else if (token == "<=")
        temp = true;
    else if (token == ">")
        temp = true;
    else if (token == ">=")
        temp = true;
    else if (token == "!=")
        temp = true;
    else if (token == "")
        temp = true;
    else if (token == "IN")
        temp = true;
    else if (token == "NOT IN")
        temp = true;
    else if (token == "BETWEEN")
        temp = true;
    else if (token == "IS")
        temp = true;
    else if (token == "IS NOT")
        temp = true;

    return temp;

}


bool is_data_type(string token)
{
    // data types includes "NULL", "INTEGER", "REAL", "TEXT", "BLOB"
    bool temp = false;
    
    if(token == "NULL")
        temp = true;
    else if (token == "INTEGER")
        temp = true;
    else if (token == "REAL")
        temp = true;
    else if (token == "TEXT")
        temp = true;
    else if (token == "BLOB")
        temp = true;
    

    return temp;
}

void is_query(string token)
{
    if(is_attribute(token))
    {
        get_token();

        if(is_comparison(token))
        {
            get_token();

            if(token[0] == '\"')
            {
                
            }
        }
        else
        {
            is_valid = false;
            cout << "ERROR: expected comparison, got \"" << token << "\"." << endl;
        }

    }
    else
    {
        is_valid = false;
        cout << "ERROR: expected attribute, got \"" << token << "\"." << endl;
    }
}

int main()
{
    string test = "first_name == \"Duncanwowee\" AND first_name == \"repear\" OR first_name == \"CREME\" + afefesfs";
    get_token();
    is_query(token);

    if(is_valid){
        cout << "CORRECT" << endl;
    }

    return 0;
}