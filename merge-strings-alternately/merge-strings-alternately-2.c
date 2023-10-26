#include <string.h>
#include <stdlib.h>

char * mergeAlternately(char * word1, char * word2){
    int i = 0, l1 = strlen(word1), l2 = strlen(word2), si = 0;
        int step = l1<=l2?l1:l2;
        char* s = (char*)calloc(l1+l2, sizeof('a'));
        while (i<step){
            s[si] = word1[i];
            si++;
            s[si] = word2[i];
            si++;
            i++;
        }
        if (l1<l2){
            while(i<l2) {
                s[si] = word2[i];
                i++;
                si++;
            }
        } else {
            while(i<l1) {
                s[si] = word1[i];
                i++;
                si++;
            }
        }
        s[si] = '\0';
        return s;
}
