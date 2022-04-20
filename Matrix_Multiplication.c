#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <time.h>
typedef long long ll;
int main(int argc, char const *argv[])
{
    int m,n,sum=0;
    int a[3][4],b[4][2],result[3][2];
    printf("Enter the elements of first matrix\n");
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            scanf("%d",&a[i][j]);
        }
        
    }
    printf("Enter the elements of second matrix\n");
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            scanf("%d",&b[i][j]);
        }
    }
    
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                sum += a[i][k] * b[k][i];
            }
            result [i][j]=sum;
            sum=0;
        }
        
    }
    printf("the resultant matrix is\n");
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            printf("%d\t",result[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}