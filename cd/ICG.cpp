#include <bits/stdc++.h>
using namespace std;
vector<string> res;
int j = 0;
vector<string> D = {"Z", "X", "Y", "W", "V", "U", "T", "S", "R", "Q", "P"};
void generate(string s)
{
    bool flag = false;
    bool flag2 = false;
    string temp = "";
    string k = "";
    string t1 = "";
    string t2 = "";
    for (auto it : s)
    {
        if (flag == false && flag2 == false)
            t1 += it;
        if (flag2 == true)
            t2 += it;
        if (it == ')')
        {
            flag2 = true;
            flag = false;
        }
        if (flag == true)
        {
            temp += it;
        }
        if (it == '(')
        {
            flag = true;
        }
    }
    if (temp != "")
    {
        cout << temp << endl;
        generate(temp);
        s = t1.substr(0, t1.size() - 1) + res[res.size() - 1][0] + t2;
    }
    temp = "";
    k = "";
    if (s[0] == '-')
    {
        string x = D[j];
        temp = x + '=' + '-' + s[1];
        res.push_back(temp);
        s = x + s.substr(2, s.size() - 2);
        j++;
    }
    for (int i = 0; i < s.length(); i++)
    {
        if ((s[i - 1] == '*' || s[i - 1] == '/' || s[i - 1] == '+' || s[i - 1] == '-') && s[i] == '-')
        {
            string x = D[j];
            temp = x + '=' + '-' + s[1];
            res.push_back(temp);
            k = s.substr(0, i - 1) + x;
            if (s.length() > i + 2)
            {
                k += s.substr(i + 2, s.size() - i - 2);
            }
            s = k;
            j++;
        }
    }
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '%')
        {
            string x = D[j];
            temp = x + '=' + s[i - 1] + s[i] + s[i + 1];
            res.push_back(temp);
            k = s.substr(0, i - 1) + x;
            if (s.length() > i + 2)
            {
                k += s.substr(i + 2, s.size() - i - 2);
            }
            s = k;
            j++;
        }
    }
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '/')
        {
            string x = D[j];
            temp = x + '=' + s[i - 1] + s[i] + s[i + 1];
            res.push_back(temp);
            k = s.substr(0, i - 1) + x;
            if (s.length() > i + 2)
            {
                k += s.substr(i + 2, s.size() - i - 2);
            }
            s = k;
            j++;
        }
    }
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '*')
        {
            string x = D[j];
            temp = x + '=' + s[i - 1] + s[i] + s[i + 1];
            res.push_back(temp);
            k = s.substr(0, i - 1) + x;
            if (s.length() > i + 2)
            {
                k += s.substr(i + 2, s.size() - i - 2);
            }
            s = k;
            j++;
        }
    }
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '+')
        {
            string x = D[j];
            temp = x + '=' + s[i - 1] + s[i] + s[i + 1];
            res.push_back(temp);
            k = s.substr(0, i - 1) + x;
            if (s.length() > i + 2)
            {
                k += s.substr(i + 2, s.size() - i - 2);
            }
            s = k;
            j++;
        }
    }
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '-')
        {
            string x = D[j];
            temp = x + '=' + s[i - 1] + s[i] + s[i + 1];
            res.push_back(temp);
            k = s.substr(0, i - 1) + x;
            if (s.length() > i + 2)
            {
                k += s.substr(i + 2, s.size() - i - 2);
            }
            s = k;
            j++;
        }
    }
    if (s[1] == '=')
        res.push_back(s);
}
void show()
{
    for (auto it : res)
    {
        cout << it << endl;
    }
}
int main()
{
    int t;
    cout << "Number of test case" << endl;
    cin >> t;
    while (t--)
    {
        string s;
        cout << "Enter a expression" << endl;
        cin >> s;
        generate(s);
        show();
        // printf("\nTarget code generation");
        // char icode[10][30], str[20], opr[10];
        // int i = 0;
        // int j = 0;
        // for (int x = 0; x < res.size(); x++)
        // {
        //     for (auto d : res[i])
        //     {
        //         icode[x][i] = d;
        //         i++;
        //     }
        // }
        
        // i=0;

        // do
        // {
        //     // strcpy(icode[i],res[i].c_str());
        //     strcpy(str, icode[i]);
        //     switch (str[3])
        //     {
        //     case '+':
        //         strcpy(opr, "ADD");
        //         break;
        //     case '-':
        //         strcpy(opr, "SUB");
        //         break;
        //     case '*':
        //         strcpy(opr, "MUL");
        //         break;
        //     case '/':
        //         strcpy(opr, "DIV");
        //         break;
        //     }

        //     printf("\nMov %c, R%d", str[2], i);
        //     printf("\n%s %c, R%d", opr, str[4], i);
        //     printf("\nMov R%d %c", i, str[0]);
        // } while (strcmp(icode[++i], "exit") != 0);

        // printf("\n");
        res.clear();
    }
    return 0;
}