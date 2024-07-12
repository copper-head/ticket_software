// Matthew Lopez
#include<iostream>
#include<string>
using namespace std;

void getToken();
bool getCorrect();
void isRelation();
void isAddOP();
void isMulOP();
void isExpression();
void isSimpleExpression();
void isTerm();
void isFactor();
void isDesign();
void isSelect();
void isAssign();
void isWriteStmt();
void isStmt();
void isStateSeq();
bool isInt(string token);
bool isDec(string token);
bool isString(string token);
bool isKeywords(string token);
bool isOperator(string token);
bool isIdentifiers(string token);
string token;
bool isValid = true;

int main()
{
    getToken();
    isStateSeq();
    if (getCorrect())
    {
        cout << "CORRECT" << endl;
    }

    return 0;
}

void getToken()
{
    cin >> token;
    return;
}

bool getCorrect()
{
    return isValid;
}

void isRelation()
{
    if (token == "<" || token == ">" || token == "=" || token == "#")
        getToken();
    else if (isValid)
    {
        cout << "INVALID!" << endl;
        cout << "Error: Relation expected, got \"" << token << "\"" << endl;
        isValid = false;
    }
    return;
}

void isAddOP()
{
    if (token == "+" || token == "-" || token == "OR" || token == "&")
        getToken();
    else if (isValid)
    {
        cout << "INVALID!" << endl;
        cout << "Error: AddOperator expected, got \"" << token << "\"" << endl;
        isValid = false;
    }
    return;
}

void isMulOP()
{
    if (token == "*" || token == "/" || token == "AND")
        getToken();
    else if (isValid)
    {
        cout << "INVALID!" << endl;
        cout << "Error: MulOperator expected, got \"" << token << "\"" << endl;
        isValid = false;
    }
    return;
}

void isExpression()
{
    isSimpleExpression();
    if (token == "<" || token == ">" || token == "=" || token == "#")
    {
        isRelation();
        isSimpleExpression();
    }
    return;
}

void isSimpleExpression()
{
    isTerm();
    while (token == "+" || token == "-" || token == "OR" || token == "&")
    {
        isAddOP();
        isTerm();
    }
    return;
}

void isTerm()
{
    isFactor();
    while (token == "*" || token == "/" || token == "AND")
    {
        isMulOP();
        isFactor();
    }
    return;
}

void isFactor()
{
    if (isInt(token) || isDec(token) || isString(token) || isIdentifiers(token))
    {
        getToken();
    }
    else if (token == "(")
    {
        getToken();
        isExpression();
        if (token == ")")
            getToken();
        else if (isValid)
        {
            cout << "INVALID!" << endl;
            cout << "Error: \")\" expected, got \"" << token << "\"" << endl;
            isValid = false;
        }
    }
    else if (token == "~")
    {
        getToken();
        isFactor();
    }
    else if (isValid)
    {
        cout << "INVALID!" << endl;
        cout << "Error: Factor expected, got \"" << token << "\"" << endl;
        isValid = false;
    }
    return;
}

void isDesign()
{
    if (isIdentifiers(token))
    {
        getToken();
        while (token == "." || token == "[")
            isSelect();
    }
    else if (isValid)
    {
        cout << "INVALID!" << endl;
        cout << "Error: Identifier expected, got \"" << token << "\"" << endl;
        isValid = false;
    }
    return;
}

void isSelect()
{
    if (token == ".")
    {
        getToken();
        if (isIdentifiers(token))
            getToken();
        else if (isValid)
        {
        cout << "INVALID!" << endl;
        cout << "Error: Identifier expected, got \"" << token << "\"" << endl;
        isValid = false;
        }
    }
    else if (token == "[")
    {
        getToken();
        isExpression();
        if (token == "]")
            getToken();
        else if (isValid)
        {
        cout << "INVALID!" << endl;
        cout << "Error: \"]\" expected, got \"" << token << "\"" << endl;
        isValid = false;
        }
    }
    else if (isValid)
    {
        cout << "INVALID!" << endl;
        cout << "Error: Selector expected, got \"" << token << "\"" << endl;
        isValid = false;
    }
    return;
}

void isAssign()
{
    isDesign();
    if (token == ":=")
    {
        getToken();
        isExpression();
    }
    else if (isValid)
    {
        cout << "INVALID!" << endl;
        cout << "Error: \":=\" expected, got \"" << token << "\"" << endl;
        isValid = false;
    }
    return;
}

void isWriteStmt()
{
    if (token == "WRITE")
    {
        getToken();
        if (token == "(")
        {
            getToken();
            isExpression();
            if (token == ")")
                getToken();
            else if (isValid)
            {
                cout << "INVALID!" << endl;
                cout << "Error: \")\" expected, got \"" << token << "\"" << endl;
                isValid = false;
            }
        }
    }
    else if (isValid)
    {
        cout << "INVALID!" << endl;
        cout << "Error: \"(\" expected, got \"" << token << "\"" << endl;
        isValid = false;
    }
  
    else if (isValid)
    {
        cout << "INVALID!" << endl;
        cout << "Error: \"WRITE\" expected, got \"" << token << "\"" << endl;
        isValid = false;
    }
    return;
}

void isStmt()
{
    if (isIdentifiers(token))
        isAssign();
    else if (token == "WRITE")
        isWriteStmt();
    else if (isValid)
    {
        cout << "INVALID!" << endl;
        cout << "Error: Statement expected, got \"" << token << "\"" << endl;
        isValid = false;
    }
    return;
}

void isStateSeq()
{
    isStmt();
    while (token == ";")
    {
        getToken();
        isStmt();
    }
    return;
}

bool isInt(string token)
{
    int state = 1;
    char c;
    for(int i = 0; i < token.length(); i++)
    {
        c = token[i];
        switch (state)
        {
            case 1:
                if(c == '-' || c == '+')
                    state = 2;
                if(c >= 48 && c <= 57)
                    state = 3;
                break;
        
            case 2:
                if(c >= 48 && c <= 57)
                    state = 3;
                else
                    state = 4;
                break;

            case 3:
                if(c >= 48 && c <= 57)
                    state = 3;
                else
                    state = 4;
                break;

            case 4:
                i = token.length() + 1;
                break;

            default:
                break;
        }
    } 
    if(state == 3)
        return true;

    return false;
}

bool isDec(string token)
{
    int state = 1;
    char c;
    for(int i = 0; i < token.length(); i++)
    {
        c = token[i];
        switch (state)
        {
            case 1:
                if(c == '-' || c == '+')
                    state = 2;
                else if(c >= 48 && c <= 57)
                    state = 3;
                else
                    state = 4;
                break;
        
            case 2:
                if(c >= 48 && c <= 57)
                    state = 3;
                else
                    state = 4;
                break;

            case 3:
                if(c >= 48 && c <= 57)
                    state = 3;
                else if(c == '.')
                    state = 5;
                else
                    state = 4;
                break;

            case 4:
                i = token.length() + 1;
                break;

            case 5:
                if(c >= 48 && c <= 57)
                    state = 6;
                else
                    state = 4;
                break;

            case 6:
                if(c >= 48 && c <= 57)
                    state = 6;
                else
                    state = 4;
                break;

            default:
                break;
        }
    }
    if(state == 6)
        return true;

    return false;
}

bool isString(string token)
{
    int i = 0, state = 1;
    char c;
    for(int i = 0; i < token.length(); i++)
    {
        c = token[i];
        switch (state)
        {
            case 1:
                if(c == 34)
                    state = 2;
                else
                    state = 4;
                break;

            case 2:
                if(!(c == 32))
                    state = 3;
                else
                    state = 4;
                break;
                
            case 3:
                if(!(c == 32) && c != 34)
                    state = 3;
                else if(c == 34)
                    state = 5;
                else
                    state = 4;
                break;

            case 4:
                i = token.length() + 1;
                break;

            default:
                break;
        }
    }
    if(state == 5)
        return true;
    return false;

}

bool isKeywords(string token)
{
    bool temp = false;
    if(token == "WRITE")
        temp = true;
    else if (token == ".")
        temp = true;
    else if (token == "[")
        temp = true;
    else if (token == "]")
        temp = true;
    else if (token == ",")
        temp = true;
    else if (token == "(")
        temp = true;
    else if (token == ")")
        temp = true;
    else if (token == ";")
        temp = true;
    
    return temp;
}

bool isOperator(string token)
{
    bool temp;
    if(token == ":=")
        temp = true;
    else if (token == "~")
        temp = true;
    else if (token == "<")
        temp = true;
    else if (token == ">")
        temp = true;
    else if (token == "=")
        temp = true;
    else if (token == "#")
        temp = true;
    else if (token == "+")
        temp = true;
    else if (token == "-")
        temp = true;
    else if (token == "OR")
        temp = true;
    else if (token == "&")
        temp = true;
    else if (token == "*")
        temp = true;
    else if (token == "/")
        temp = true;
    else if (token == "AND")
        temp = true;
    
    return temp;
}

bool isIdentifiers(string token)
{
    int state = 1;
    char c;
    for(int i = 0; i < token.length(); i++)
    {
        c = token[i];
        switch (state)
        {
            case 1:
                if((c >= 65 && c <= 90) || (c >= 97 && c <= 122))
                    state = 2;
                else
                    state = 3;
                break;
            
            case 2:
                if((c >= 65 && c <= 90) || (c >= 97 && c <= 122))
                    state = 2;
                else if(c >= 48 && c <= 57)
                    state = 2;
                else
                    state = 3;
                break;
                
            case 3:
                i = token.length() + 1;
                break;

            default:
                break;
        }
    }
    if(isKeywords(token) == true)
        return false;
    if(state == 2)
        return true;
    return false;
}