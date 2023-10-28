#include <string.h>
#include <stdio.h>
#include <stdbool.h>
bool isSubsequence(char * s, char * t){
    int i = 0, c= 0;
    char* hi;
    while(i<strlen(s)){
        hi = strchr(t+c, s[i]);
        if(hi==0){
            return false;
        } else{
            c = hi-t+1;
        }
        i++;
    }
    return true;
}
