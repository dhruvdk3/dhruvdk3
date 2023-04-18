#include <bits/stdc++.h>
using namespace std;

vector <string> productions {
    "S=aABb",
    "A=c",
    "A=#",
    "B=d",
    "B=#",
};

char table [4][7] = {
    "-abcd$",
    "S     ",
    "A     ",
    "B     "
};
string follow [] = {
    "",
    "$",
    "db",
    "b"
};

int main (){
    unordered_map<char, int> M;
    M['S'] = 1; 
    M['A'] = 2;
    M['B'] = 3;
    M['a'] = 1;
    M['b'] = 2;
    M['c'] = 3;
    M['d'] = 4;
    M['$'] = 5;

    for(int i = 0 ; i <productions.size(); i++){
        string temp = productions[i];
        int row = M[temp[0]];
        
        int column = 0;
        if(temp[2]=='a' || temp[2]=='c' || temp[2]=='d'){            
            column = M[temp[2]];
            table[row][column] = char(i+('0')+1);
        }
        if(temp[2]=='#'){
            string getFollow = follow[M[temp[0]]];
            for(int j = 0 ; j<getFollow.length() ; j++){
                column = M[getFollow[j]];
                table[row][column] = char(i+('0')+1);
            }
        }

    }
    for(int i = 0 ; i < 4 ; i++){
        for(int j = 0 ; j < 7 ; j++){
            cout<<table[i][j]<<" ";
        }
        cout<<endl;
    }

}