#include <bits/stdc++.h>
using namespace std;

#define SUCCESS 1
#define FAILED 0


int X(), Y(), Z(), W();
const char *cursor;
// char string[64];

int main()
{
    char st[64];
    puts("Enter the string");
    cin >> st;
    cursor = st;
    puts("");
    puts("Input		 Action");
    puts("--------------------------------");

    if (X() && *cursor == '\0')
    {
        puts("--------------------------------");
        puts("String is successfully parsed");
        return 0;
    }
    else
    {
        puts("--------------------------------");
        puts("Error in parsing String");
        return 1;
    }
}

int X(){
    if (*cursor == 'x')
    {
        printf("%-16s X -> xY'\n", cursor);
        cursor++;
        if (Y()){
            return SUCCESS;
        }
        else
            return FAILED;
    }
    else
        return FAILED;
}

int Y(){
    if(Z()){
        printf("%-16s Y->ZwY\n", cursor);
        if (*cursor == 'w')
        {
            cursor++;
            if(Y()){
                return SUCCESS;
            }
            else
                return FAILED;
        }
        else
            return FAILED;
        
    }

    else if(*cursor == 'x'){
        printf("%-16s Y->xY\n", cursor);
        cursor++;
        if(Y()){
            return SUCCESS;
        }
        else
            return FAILED;
    }
    else{
        printf("%-16s Y->$\n", cursor);
        return SUCCESS;
    }
    
}

int Z(){
    if(*cursor == 'y'){
        printf("%-16s Z->yW\n",cursor);
        cursor++;
        if(W()){
            return SUCCESS;
        }
        else 
            return FAILED;
    }
    else 
            return FAILED;
}

int W(){
    if(*cursor == 'w'){
        printf("%-16s W->zW\n");
        cursor++;
        if(W()){
            return SUCCESS;
        }
        else 
            return FAILED;
    }
    else {
        printf("%-16s W->$\n",cursor);
        return SUCCESS;
    }
}
