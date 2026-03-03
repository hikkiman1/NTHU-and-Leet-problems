#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    const char *timePoints[] = {"23:59","00:00"};
    int length = sizeof(timePoints) / sizeof(timePoints[0]);
    int hours1, minutes1;
    int hours2, minutes2;
    int final = 1440;
    for (int i = 0; i < length; i++){
        sscanf(timePoints[i], "%d:%d", &hours1, &minutes1);
        for (int j = i+1; j < length; j++){
            sscanf(timePoints[j], "%d:%d", &hours2, &minutes2);
            int interval = abs(hours1*60 + minutes1 - hours2*60 - minutes2);
            int ans = ((interval)
            < (1440 - interval) ? (interval):(1440 - interval));
            final = ((ans) < (final) ? (ans):(final));
        }
    }
    printf("%d", final);
    return 0;

}