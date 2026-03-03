#include <stdio.h>

int main(){
    long long a, b, c;
    long long money = 10000;

    while (scanf("%lld %lld %lld", &a, &b, &c) == 3){
        if (money <= 0){
            printf("No balance\n");
        } else {
            if (a > b){
                money += c;
            } else if (a < b){
                money -= c;
                if (money <= 0){
                    printf("0\n");
                } 
            }
        }        
    }
    if (money > 0){
        printf("%lld\n", money);
    }
    return 0;
    }