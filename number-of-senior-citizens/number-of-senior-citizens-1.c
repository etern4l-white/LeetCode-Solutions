#include <stdlib.h>
#include <string.h>

int countSeniors(char ** details, int detailsSize){
    int i = 0, s = 0, c = 0;
    char hi[3];
    while(i<detailsSize){
        strncpy(hi, &(details[i][11]), 2);
        c = atoi(hi);
        s+=c>60?1:0;
        i++;
    }
    return s;
}
