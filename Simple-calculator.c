#include <stdlib.h>
#include <stdio.h>
#include <string.h> 
#include <math.h>
#include <time.h>
typedef long long ll;
int main(int argc, char *argv[])
{
    char *operation;
    int num1,num2;
    operation =argv[1];
    num1 =atoi(argv[2]);
    num2 =atoi(argv[3]);
    printf("operation is %s\n",operation);
    printf("num1 is %d\n",num1);
    printf("num2 is %d\n",num2);
    if (strcmp(operation,"add")==0){
        printf("%d\n",num1+num2);
    }
    else if (strcmp(operation,"substract")==0){
        printf("%d\n",num1-num2);
    }
    else if (strcmp(operation,"multiply")==0){
        printf("%d\n",num1*num2);
    }
    else if (strcmp(operation,"divide")==0){
        printf("%d\n",num1/num2);
    }
    return 0;
}