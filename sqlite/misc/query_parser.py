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

# Description:
#       This function is used to check that validity of paramaters
#
def parse_string_conditional(input_str, valid_params, valid_cond):
    
    # Terminal Rules for the grammar.
    param = pp.oneOf(valid_params)
    comparators = pp.oneOf(valid_cond)
    logical_ops = pp.oneOf("AND OR")
    not_op = pp.oneOf("NOT")

    tail_rule = pp.Forward()
    
    # 
    conditionals = pp.Optional(not_op) + param + comparators + string_token
    tail_rule << (logical_ops + conditionals + pp.Optional(tail_rule))
    start_rule = conditionals + pp.Optional(tail_rule)

    # parse the input string
    try:
        result = start_rule.parseString(input_str)
        joined_result = " ".join(result)
    except:
        return False

    return joined_result

    


if __name__ == "__main__":

    input_str = "first_name == \"Duncanwowee\" AND first_name == \"repear\" OR first_name == \"CREME\" + afefesfs"

    test = parse_string_conditional(input_str, "first_name", "==")

    print(test)
    print(" ".join(test))
    
