#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <time.h>
typedef long long ll;
int gran(){
    srand(time(NULL));
    return rand()%3;
}
int greater(char c1, char c2){
    if ((c1=='r' && c2=='s') || (c1=='p' && c2=='s') || (c1=='s' && c2=='p'))
    {
        return 1;
    }
    else if (c1==c2){
        return -1;
    }
    else {
        return 0;
    }
}
int main(int argc, char const *argv[])
{
    int scorep=0,temp,t2;
    int scorec=0;
    char playerchar, compchar;
    char dict[]={'r','p','s'};
    printf("Welcome to the game");
    printf("Choose 1 for rock 2 for paper 3 for scissor\n");
    for (int i = 0; i < 3; i++)
    {
        scanf("%d",&temp);
        playerchar=dict[temp-1];
        printf("You choose %d\n",temp);
        printf("You choose %c\n",playerchar);

        printf("Computers turn\n");
        t2=gran()+1;
        printf("%d\n",t2);
        compchar=dict[t2-1];
        printf("Computer choose %c\n",compchar);


        if (greater(compchar,playerchar)==1)
        {
            scorec++;
        }
        else  if (greater(compchar,playerchar)==-1)
        {
            scorep++;
        }
        else
        {
            scorep++;
        }
        
    }
    if (scorep > scorec)
    {
        printf("You win");
    }
    else if (scorep < scorec)
    {
        printf("You Loose");
    }
    else
    {
        printf("its a draw");
    }
    
    return 0;
}
