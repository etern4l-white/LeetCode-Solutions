#include <limits.h>
int largestAltitude(int* gain, int gainSize){
    int m = INT_MIN, i =0, s = 0;
    while(i<gainSize){
        s+=gain[i];
        m = s>m?s:m;
        i++;
    }
    return m>0?m:0;
}
