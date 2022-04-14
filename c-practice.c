#include <stdlib.h>
#include <stdio.h>
#include <string.h>
typedef long long ll;
void parser(char* string){
    int in=0;
    int index=0;
    for (int i = 0; i < strlen(string); i++)
    {
        if (string[i]=='<')
        {
            in=1;
            continue;
        }
        else if (string[i]=='>')
        {
            in=0;
            continue;
        }
        if (in==0)
        {
            string[index]=string[i];
            index++;
        }
        
    }
    string[index]='\0';
    while (string[0]==' ')
    {
        for (int j = 0; j < strlen(string); j++)
        {
            string[j]=string[j+1];
        }
        
    }
    while (string[strlen(string)-1]==' ')
    {
        string[strlen(string)-1]='\0';
    }
    
    
}
int main(int argc, char const *argv[])
{
    char string[]="<p>    This is a paragraph   </p>";
    parser(string);
    printf("THe parsed string is ~~%s~~",string);
    return 0;
}