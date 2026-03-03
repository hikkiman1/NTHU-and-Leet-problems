#include <stdio.h>

int main(){
    int ph, pm, ps;
    scanf("%d %d %d", &ph,&pm,&ps);
    int ch, cm, cs;
    scanf("%d %d %d", &ch,&cm,&cs);
    int ih, im, is;
    if (ps >= cs){
        is = ps - cs;
    } else {
        is = ps + 60 - cs;
        cm += 1;
    }
    if (pm >= cm){
        im = pm - cm;
    } else {
        im = pm + 60 - cm;
        ch += 1;
    }
    if (ph >= ch){
        ih = ph - ch;
    } else {
        ih = ph + 24 - ch;
    }
    printf("%02d %02d %02d", ih, im ,is);
    return 0;
    }