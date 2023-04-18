#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define ll long long
#define all(x) x.begin(), x.end()
map<char, vector<string>> mp;
multimap<int, string> table;
vector<string> numbering(0);
vector<vector<string>> collection(1);
unordered_map<char, string> first, _follow;

void First_terminal()
{
    for (auto i : mp)
    {
        for (auto i1 : i.second)
        {
            if (!(i1[0] >= 65 && i1[0] <= 90))
                first[i.first].push_back(i1[0]);
        }
    }
}
void Follow()
{
    for (auto i : mp)
    {
        for (auto i1 : i.second)
        {
            for (int stp = 0; stp < i1.size(); stp++)
            {
                if ((i1[stp] >= 65 && i1[stp] <= 90))
                {

                    if (stp + 1 == i1.size())
                    {
                        for (auto t : _follow[i.first])
                            _follow[i1[stp]].push_back(t);
                    }
                    else
                    {

                        int stp1 = stp + 1;
                        if (i1[stp1] >= 65 && i1[stp1] <= 90)
                        {
                            for (auto t : first[i1[stp1]])
                                _follow[i1[stp]].push_back(t);
                        }
                        else
                        {
                            _follow[i1[stp]].push_back(i1[stp1]);
                        }
                    }
                }
            }
        }
    }
    first.clear();
}
void Del()
{
    for (auto &i : _follow)
    {
        set<char> st;
        for (auto it : i.second)
        {
            st.insert(it);
        }
        i.second.erase();
        for (auto it : st)
            i.second.push_back(it);
    }
}
int FindInd(string s)
{
    for (int i = 0; i < numbering.size(); i++)
    {
        if (numbering[i] == s)
            return i + 1;
    }
    return -1;
}
int FindInd1(vector<string> temp)
{
    for (int i = 0; i < collection.size(); i++)
    {
        if (collection[i] == temp)
            return i;
    }
    return -1;
}
void Productions(vector<string> &temp, char c)
{
    if (c >= 65 && c <= 90)
    {
        queue<char> q;
        q.push(c);
        while (!q.empty())
        {
            q.pop();
            for (auto i : mp[c])
            {
                string x = "-.";
                if (count(all(temp), c + x + i))
                    break;
                temp.push_back(c + x + i);
                if (i[0] >= 65 && i[0] <= 90)
                    q.push(i[0]);
            }
            c = q.front();
        }
        return;
    }
    else
        return;
}
void Collections()
{
    int i = 0;
    vector<string> t(0);
    t.push_back("Z-.S");
    Productions(t, 'S');
    collection.push_back(t);

    while (i < collection.size())
    {
        for (auto j : collection[i])
        {
            for (int cnt = 0; cnt < j.size(); cnt++)
            {

                if (j[cnt] == '.')
                {
                    string sp = "";
                    if (cnt + 1 == j.size())
                    {
                        for (auto ch : _follow[j[0]])
                        {
                            sp = to_string(FindInd(j.substr(0, j.size() - 1))) + ch + "r";
                            table.insert({i, sp});
                        }
                    }
                    else
                    {
                        vector<string> temp(0);
                        temp.push_back(j.substr(0, cnt) + j[cnt + 1] + '.' + j.substr(cnt + 2, j.size()));
                        if (cnt + 2 < j.size())
                            Productions(temp, j[cnt + 2]);
                        int ind = FindInd1(temp);
                        if (ind != -1)
                        {
                            sp = to_string(ind);
                            sp += j[cnt + 1];
                            if (!(j[cnt + 1] >= 65 && j[cnt + 1] <= 90))
                                sp += "s";
                        }
                        else
                        {
                            collection.push_back(temp);
                            sp = to_string(collection.size() - 1);
                            sp += j[cnt + 1];
                            if (!(j[cnt + 1] >= 65 && j[cnt + 1] <= 90))
                                sp += "s";
                            // cout<<i<<" on "<<j[cnt+1]<<" go to "<<to_string(collection.size()-1)<<endl;
                        }

                        table.insert({i, sp});
                    }
                }
            }
        }
        i++;
    }
    mp.clear();
}
string FindAction(char ch, char t)
{
    for (auto i : table)
    {
        if (i.first == ch - '0')
        {
            if (i.second[1] == t)
            {
                return i.second;
            }
        }
    }
    return "-";
}
string Check(string s)
{
    stack<char> stk;
    stk.push('1');
    int ptr = 0, c = 0;
    while (!stk.empty())
    {
        cout << endl
             << endl;
        // cout<<stk.top();
        string action = FindAction(stk.top(), s[ptr]);
        if (action == "-")
        {
            cout << "Action is not Valid : BREAK\n";
            break;
        }

        // cout<<stk.top()<<" on "<<s[ptr]<<" goes to "<<action[0]<<" action :"<<action[2]<<endl;
        if (action[2] == 'r')
        {
            cout << stk.top() << " on " << s[ptr] << " action is :r" << action[0] << endl;
            cout << "production is : " << numbering[(action[0] - '0') - 1] << endl;

            if (stk.size() <= 2 * (numbering[(action[0] - '0') - 1].size() - 2))
            {
                cout << "Size of Stack is Less : Breaking \n";
                break;
            }

            for (int cnt = 0; cnt < 2 * (numbering[(action[0] - '0') - 1].size() - 2); cnt++)
            {
                cout << stk.top() << " will be popped \n";
                stk.pop();
            }
            string action1 = FindAction(stk.top(), numbering[(action[0] - '0') - 1][0]);
            stk.push(numbering[(action[0] - '0') - 1][0]);
            cout << "push: " << stk.top() << " " << action1[0] << endl;
            stk.push(action1[0]);
        }

        else if (action[2] == 's')
        {
            cout << stk.top() << " on " << s[ptr] << " is in Item :" << action[0] << " action: " << action[2] << endl;
            cout << "collection is: ";
            for (auto i : collection[action[0] - '0'])
                cout << i << " , ";

            cout << endl;
            if (ptr == s.size())
            {
                cout << "Size of Sting less : BREAK\n";
                break;
            }
            cout << "PUSH: " << s[ptr] << " " << action[0] << "\nincrement pointer " << endl;
            stk.push(s[ptr]);
            ptr++;
            stk.push(action[0]);
        }

        else if (action[2] == '.')
        {
            cout << stk.top() << " on " << s[ptr] << " action: " << action[2] << endl;
            for (auto i : collection[action[0] - '0'])
                cout << i << " , ";

            cout << endl;
            return "Accepted";
        }
    }
    return "\nNot Accepted";
}
int main()
{
    cout << "Enter No of Productions  & Grammer : " << endl;
    int size;
    cin >> size;
    string s;
    for (int i = 0; i < size; i++)
    {
        cin >> s;
        numbering.push_back(s);
        mp[s[0]].push_back(s.substr(2, s.size()));
    }
    numbering.push_back("Z-S");

    int cnt = 0;
    mp['Z'].push_back("S");
    _follow['S'].push_back('#');
    _follow['Z'].push_back('#');
    First_terminal();
    Follow();
    cout << "        ACTION                              GOTO         " << endl;
    cout << "   a             b            $          A            S   " << endl;
    cout << "0   S3             S4                    2            1   " << endl;
    cout << "1                         accepted                    " << endl;
    cout << "2   S3             S4                    5                " << endl;
    cout << "3   S3             S4                    6                 " << endl;
    cout << "4   R3             R3           R3                          " << endl;
    cout << "5                               R1                         " << endl;
    cout << "6   R2             R2           R2                        " << endl;

    Del();
    Collections();
    cout << "\n follow :\n";
    for (auto i : _follow)
    {
        cout << i.first << " - " << i.second << endl;
    }
    cout << "\n\ntotal number of collections " << collection.size() - 1 << "\ncollections :";
    for (auto i : collection)
    {
        for (auto j : i)
        {
            cout << j << ",";
        }
        cout << endl
             << endl;
    }

    // cout << "\n\n\ntable is : \n";
    // for (auto &i : table)
    // {
    //     if (i.first == 2)
    //     {
    //         if (i.second == "4#r")
    //         {
    //             i.second = "4#.";
    //         }
    //     }
    //     cout << i.first;
    //     if (i.second[2] == 'r')
    //         cout << " Reducing to Production : ";
    //     else
    //         cout << " Shifting to Collection : ";
    //     cout << i.second[0] << " on " << i.second[1] << " action : " << i.second[2];
    //     cout << endl;
    // }
    mp.clear();
    first.clear();
    _follow.clear();
    cout<<"Enter the string :";
    cin >> s;
    cout << Check(s);
    return 0;
}