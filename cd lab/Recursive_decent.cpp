#include <bits/stdc++.h>
using namespace std;

#define SUCCESS 1
#define FAILED 0

int S(), PDash(), Q(), Rdash();

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

    if (S() && *cursor == '\0')
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

int S()
{
    if (*cursor == 'x')
    {
        printf("%-16s S → xP'\n", cursor);
        cursor++;
        if (PDash())
        {
            return SUCCESS;
        }
        else
            return FAILED;
    }
    else
        return FAILED;
}

int PDash()
{
    if (Q())
    {
        printf("%-16s P’ → QzP'\n", cursor);
        if (*cursor == 'z')
        {
            cursor++;
            if (PDash())
                return SUCCESS;
            else
                return FAILED;
        }
        else
            return FAILED;
    }
    else if (*cursor == 'x')
    {
        printf("%-16s P' -> xP'\n", cursor);
        cursor++;
        if (PDash())
        {
            return SUCCESS;
        }
        else
            return FAILED;
    }
    else
    {
        printf("%-16s P' -> $\n", cursor);
        return SUCCESS;
    }
}

int Q()
{
    if (*cursor == 'y')
    {
        printf("%-16s Q → yR’\n", cursor);
        cursor++;
        if (Rdash())
            return SUCCESS;
        else
            return FAILED;
    }
    else
        return FAILED;
}

int Rdash()
{
    if (*cursor == 'w')
    {
        printf("%-16s R’ → wR’\n", cursor);
        cursor++;
        if (Rdash())
        {
            return SUCCESS;
        }
        else
            return FAILED;
    }
    else
    {
        printf("%-16s B'->$\n", cursor);
        return SUCCESS;
    }
}