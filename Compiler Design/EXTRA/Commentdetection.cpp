#include <bits/stdc++.h>
using namespace std;
int main (){
    vector<string> lines ;

    bool isComment = false;
    while(true){
        string temp;
        getline(cin,temp);
        if(temp.length()==0) break;
        lines.push_back(temp);
        if(temp[0]=='/' && temp[1]=='/'){
            break;
        }
        int length = temp.length();
        if(temp[length-2] == '*' && temp[length-1]=='/'){
            break;
        }
    }
    int size = lines.size();
    if(lines.size()==1){
        if(lines[0].length()>=2){
            if(lines[0][0]=='/' &&lines[0][1] == '/'){
                isComment = true;
            }
            int length = lines[0].length();
            if(length >= 4){
                if(lines[0][0]=='/' && lines[0][1] =='*' && lines[0][length-2] =='/' && lines[0][length-1] ){
                    isComment = true;
                }
            }
        }
    }
    
    else{
        if(lines[0][0]=='/' && lines[0][1] == '/'){
            int check = 0 ;
            for(auto it : lines){
                if(it[0]!='/' && it[1]!='/'){
                    check = - 1;
                    isComment = false;
                    break;
                }
            }
            if(check!=-1){
                isComment = true;
            }
        }
        else{
            if(lines[0][0]=='/' && lines[0][1] == '*'){
                string temp = lines[size-1];
                int length = temp.length();
                if(temp[length-2] == '*' && temp[length-1] =='/'){
                    isComment = true;
                }
            }
        }
    }
    if(isComment){
        cout<<"Its a comment!";
    }
    else{
        cout<<"It's not a comment";
    }
}

