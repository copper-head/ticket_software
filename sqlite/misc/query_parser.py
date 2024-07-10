import pyparsing as pp

# Author: Duncan Truitt
# 
# The purpose of this file is to hold functions that we will use to 
# parse the validty of certain arguments passed by users through the API.
# For example, consider the situation where we would like users to be able
# to specify conditions on a SELECT operation where they can pass as a param
# something like 'user_name == "bob" and is_enabled == 1'. We need to
# accomplish two things in parsing this:
#
#       1. Is the input valid?
#       2. Is the user attempting to exploit something (SQL injection attack)?
#
# If the input is acceptable, then the input will be run in a SQL query.
#
# Luckily for us the input we will need to parse will only require a fairly
# simple grammar as we are going to follow this format:
#
# ([attribute] [conditional] [data_type]) ([logical_op] [attribute] [condtional] [data_type])

string_token = pp.Regex(r'"[^" | ^\"]*"')

def string_conditional(input_str, valid_params, valid_cond):
    
    # Rules for params and comparators
    param = pp.oneOf(valid_params)
    comparators = pp.oneOf(valid_cond)
    
    # Terminal Rule
    condtionals = param + comparators + string_token

    # parse the input string
    try:
        result = condtionals.parseString(input_str)
    except:
        return False

    if len(result) == 3:
        return result
    else:
        return False


if __name__ == "__main__":

    input_str = "first_name \"Duncan\"\"wowee\""

    test = string_conditional(input_str, "first_name", "==")

    print(test)
    
