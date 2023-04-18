using namespace std;


  // 17.4.1.2 Headers

  // C
  #ifndef _GLIBCXX_NO_ASSERT
  #include <cassert>
  #endif
  #include <cctype>
  #include <cerrno>
  #include <cfloat>
  #include <ciso646>
  #include <climits>
  #include <clocale>
  #include <cmath>
  #include <csetjmp>
  #include <csignal>
  #include <cstdarg>
  #include <cstddef>
  #include <cstdio>
  #include <cstdlib>
  #include <cstring>
  #include <ctime>

  #if __cplusplus >= 201103L
  #include <ccomplex>
  #include <cfenv>
  #include <cinttypes>
  #include <cstdbool>
  #include <cstdint>
  #include <ctgmath>
  #include <cwchar>
  #include <cwctype>
  #endif

  // C++
  #include <algorithm>
  #include <bitset>
  #include <complex>
  #include <deque>
  #include <exception>
  #include <fstream>
  #include <functional>
  #include <iomanip>
  #include <ios>
  #include <iosfwd>
  #include <iostream>
  #include <istream>
  #include <iterator>
  #include <limits>
  #include <list>
  #include <locale>
  #include <map>
  #include <memory>
  #include <new>
  #include <numeric>
  #include <ostream>
  #include <queue>
  #include <set>
  #include <sstream>
  #include <stack>
  #include <stdexcept>
  #include <streambuf>
  #include <string>
  #include <typeinfo>
  #include <utility>
  #include <valarray>
  #include <vector>

  #if __cplusplus >= 201103L
  #include <array>
  #include <atomic>
  #include <chrono>
  #include <condition_variable>
  #include <forward_list>
  #include <future>
  #include <initializer_list>
  #include <mutex>
  #include <random>
  #include <ratio>
  #include <regex>
  #include <scoped_allocator>
  #include <system_error>
  #include <thread>
  #include <tuple>
  #include <typeindex>
  #include <type_traits>
  #include <unordered_map>
  #include <unordered_set>
  #endif
using namespace std;
vector<string> p(0);
bool datatype(string t)
{
    p = {"int", "string", "char", "char*", "bool", "float", "double", "long", "long long"};
    for (auto i : p)
    {
        if (t == i)
        {
            return true;
        }
    }
    return false;
}

bool keyword(string t)
{
    p = {"main", "if", "else", "for", "void", "return", "cin", "cout"};
    for (auto i : p)
    {
        if (i == t)
        {
            return true;
        }
    }
    return false;
}

bool op(string t)
{
    p = {"+", "-", "=", "==", "&&", "||", "?", ":", "::", ">>", "<<", "!=","!", ">=" , "<=" , "&" , "|" ,"^"};
    for (auto i : p)
    {
        if (i == t)
        {
            return true;
        }
    }
    return false;
}
bool sep(string t)
{
    p = {",", ";"};
    for (auto i : p)
    {
        if (t == i)
        {
            return true;
        }
    }
    return false;
}

bool par(string t)
{
    p = {"{", "()", "}", "[]", "[", "]", "{}", "(", ")"};
    for (auto i : p)
    {
        if (t == i)
        {
            return true;
        }
    }
    return false;
}

bool id(string t)
{
    if (isalpha(t[0]) || t[0] == '_')
    {
        return true;
    }
    return false;
}
int main()
{
    string s, t = "";
    int cnt = 0, cnt_token = 0;
    vector<string> dt(0), idf(0);
    bool chk = 0, chkd = 1, eq = 0;

    while (getline(cin, s))
    {
        if (s[0] == '/' && s.size() > 1)
        {
            if (s[1] == '/')
                cout << s << " comment\n";
            else if (s[1] == '*')
            {
                t += s;
                chk = 1;
                if (s[s.size() - 1] == '/' && s[s.size() - 2] == '*')
                {
                    cout << t << " comment\n";
                    t = "";
                    chk = 0;
                }
            }
        }
        else if (chk)
        {
            t += s;
            if (s.back() == '/' && s[s.size() - 2] == '*')
            {
                cout << t << " comment\n";
                t = "";
                chk = 0;
            }
        }
        else
        {
            s.push_back(' ');
            for (auto i : s)
            {
                if (i != ' ')
                {
                    t += i;
                }
                else
                {
                    if (t.size())
                    {
                        if (datatype(t))
                        {
                            cout << t << " datatype\n", chkd = 1, cnt_token++;
                        }
                        else if (keyword(t))
                        {
                            cout << t << " keyword\n", cnt_token++;
                        }
                        else if (op(t))
                        {
                            cout << t << " operator\n", cnt_token++;
                            if (t == "=")
                            {
                                eq = 1;
                            }
                        }
                        else if (sep(t))
                        {
                            cout << t << " Separator\n", cnt_token++;
                        }
                        else if (par(t))
                        {
                            cout << t << " Parenthesis\n", cnt_token++;
                        }
                        else if (id(t))
                        {
                            if (chkd)
                            {
                                cout << t << " Identifier\n", chkd = 0, cnt_token++;
                                idf.push_back(t);
                            }
                            else
                            {
                                bool c = 0;
                                for (auto i : idf)
                                {
                                    if (t == i)
                                    {
                                        c = 1, cnt_token++;
                                    }
                                }
                                if (!c)
                                {
                                    if (t[0] >= 'a' && t[0] <= 'z')
                                    {
                                        cout << t << " Identifier" << endl;
                                        cnt_token++;
                                    }
                                    else if (t[0] >= 'A' && t[0] <= 'Z')
                                    {
                                        cout << t << " Identifier" << endl;
                                        cnt_token++;
                                    }
                                    else{
                                        cout << t << " Not a valid identifier\n";
                                    }
                                }
                            }
                        }
                        else if (eq)
                        {
                            cout << t << " Value\n", cnt_token++;
                            eq = 0;
                        }
                        else
                        {
                            if (t[0] >= '0' && t[0] <= '9' && t[t.length()-1 ] >= '0' && t[t.length()-1] <='9' )
                            {
                                bool flag1 = true;
                                for(int i = 0 ; i < t.length() ; i ++){
                                    if(t[i]>='a' && t[i]<='z'){
                                        flag1 = false;
                                        break;
                                    }
                                    if(t[i]>='A' && t[i]<='B'){
                                        flag1 = false;
                                        break;
                                    }
                                }
                                if(flag1){
                                    cout << t << " Value" << endl;
                                    cnt_token++;
                                }
                                else{
                                    cout<<t<<" Invalid"<<endl;
                                }
                            }
                            else if (t[0] >= 'a' && t[0] <= 'z')
                            {
                                cout << t << " It's an identifer" << endl;
                                cnt_token++;
                            }
                            else if (t[0] >= 'A' && t[0] <= 'Z')
                            {
                                cout << t << " It's an identifer" << endl;
                                cnt_token++;
                            }
                            else
                            {
                                cout << t << " invalid\n";
                            }
                        }
                        t = "";
                    }
                }
            }
        }
    }
    cout << "\n Total tokens : " << cnt_token;
    return 0;
}
