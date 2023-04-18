#include <bits/stdc++.h>
using namespace std; 

int main (){

    vector<string> lines;
    bool isComment = false;

    while(true){
        string temp = "";
        getline(cin,temp);
        if(temp.length()==0){
            break;
        }
        lines.push_back(temp);
    }

    // Searching for single line & multi-line comment
    bool multilineStart = false;
    bool mutlilineEnd =false;

    for(int i = 0 ; i < lines.size() ; i ++){
        for(int j = 0 ; j < lines[i].length() ; j ++){
            if(j+1 < lines[i].length()){
                if(lines[i][j]=='/' && lines[i][j+1]=='/'){
                    isComment = true;
                }
                if(lines[i][j]=='/' && lines[i][j+1]=='*'){
                    multilineStart = true;
                }
                if(lines[i][j]=='*' && lines[i][j+1]=='/'){
                    mutlilineEnd = true;
                }
            }
        }
    }
    cout<< ((isComment) || (multilineStart&&mutlilineEnd));
}
