#include <stdio.h>


int main(){
    int interval;
    char line[6];
    scanf("%d %s", &interval, &line);
    for (int i = 0; i < 5; i++){
        line[i] = (line[i] - 'a' + interval)%26 + 'A';
    }
    printf("%s", line);
    return 0;

}