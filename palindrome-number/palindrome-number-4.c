#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <stdio.h>


bool isPalindrome(int x) {
    if (x<0) return false;
    char ss[11*sizeof(char)];
    sprintf(ss, "%d", x);
    int lenn = strlen(ss);
    for(int i = 0; i<lenn/2; i++) {
        if (i==0 && !(x%(int)(pow(10, i+1)) == ( x%(int)(pow(10, lenn-i)) - x%(int)(pow(10, lenn-i-1))  )/(int)(pow(10, lenn-i-1))   )) return false;
        else {
            if (!((x%(int)(pow(10, i+1)) - x%(int)(pow(10, i)))/(int)(pow(10, i)) == ( x%(int)(pow(10, lenn-i)) - x%(int)(pow(10, lenn-i-1))  )/(int)(pow(10, lenn-i-1))   )) {
                return false;
            }
        }
    }

    return true;
}
