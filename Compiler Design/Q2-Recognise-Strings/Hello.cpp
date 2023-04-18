#include <bits/stdc++.h>
using namespace std;

int main () {
    
    int startingA = 0 ;
    int B_s = 0;
    int endingA = 0 ;
    bool flag = true;
    
    string s  ;
    cin >> s ;

    for(int i = 0 ; i < s.length() ; i ++){
        if( (s[i]=='a') && (B_s==0) && (endingA==0)){
            startingA ++ ;
        }
        else if ( s[i]=='b' && endingA == 0 ){
            B_s++;
        }
        else if (s[i]=='a' && (B_s>=2)){
            endingA ++ ;
        }
        else{
            flag = false;
        }
    }

    if(flag && ((startingA + B_s + endingA) == s.length()) && (B_s>=2) ){
        cout<<"Matches";
    }
    else{
        cout<<"Does not match";
    }

}
