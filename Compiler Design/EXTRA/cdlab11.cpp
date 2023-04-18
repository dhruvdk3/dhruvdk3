#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
int getop(char c)
{
    if (c == '+')
    {
        return 1;
    }
    else if (c == '-')
    {
        return 2;
    }
    else if (c == '*')
    {
        return 3;
    }
    else if (c == '/')
    {
        return 4;
    }
    else
    {
        return 5;
    }
}

int main()
{
    int op = 0;
    cout << "Enter an expression\n";
    string s;
    cin >> s;
    cout << s << endl;
    for (int i = 0; i < s.size(); i++)
    {
        if (getop(s[i]) != 5)
        {
            op = getop(s[i]);
        }
    }
    if (op == 0 or s[1] != '=' or s[0] < 'a' or s[0] > 'z' or s.find("++") != string::npos)
    {
        cout << "Please enter a valid expression\n";
    }
    else
    {
        cout << "MOV"
             << " " << s[s.size() - 3] 
             << " R1 "<< '\n';
        cout << "MOV"
             << " " << s[s.size() - 1] 
             << " R2 "<< '\n';
        if (op == 1)
        {
            cout << "ADD"
                 << " R1 "
                 << " R2\n";
        }
        else if (op == 2)
        {
            cout << "SUB"
                 << " R1 "
                 << " R2\n";
        }
        else if (op == 3)
        {
            cout << "MUL"
                 << " R1 "
                 << " R2\n";
        }
        else if (op == 4)
        {
            cout << "DIV"
                 << " R1 "
                 << " R2\n";
        }
    for (int i =s.size()-1; i>=0; i--)
    {
        if (getop(s[i]) != 5)
        {
            op = getop(s[i]);
        }
    }
    if (op == 0 or s[1] != '=' or s[0] < 'a' or s[0] > 'z' or s.find("++") != string::npos)
    {
        cout << "Please enter a valid expression\n";
    }
    else
    {
        cout << "MOV"
             << " " << s[s.size() - 5]
             << " R2 "<<'\n';
        // cout << "MOV"
        //      << " R2 "
        //      << " " << s[s.size() - 3] << '\n';
        if (op == 1)
        {

            cout << "ADD"
                 << " R1 "
                 << " R2\n";
        }
       else if (op == 2)
        {
            cout << "SUB"
                 << " R1 "
                 << " R2\n";
        }
        else if (op == 3)
        {
            cout << "MUL"   
                 << " R1 "
                 << " R2\n";
        }
        else if (op == 4)
        {
            cout << "DIV"
                 << " R1 "
                 << " R2\n";
        }

        else
        {
            cout << "Invalid input\n";
        }

        cout << "MOV " << s[0] << " R1\n";
    }
    }

    return 0;
}