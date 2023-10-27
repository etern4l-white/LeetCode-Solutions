#include <stdlib.h>
#include <string.h>


// char* delete_string(char* org, char* rep, int rep_len) {
//     char* strr = strdup(org);
//     char* substrr = strdup(rep);
//     char* first_point = strstr(strr, substrr);
//     while (first_point != NULL) {

//         char* new_str = (char*)calloc(strlen(strr)+1, sizeof('a'));
//         strncat(new_str, strr, first_point - strr);
//         new_str[first_point - strr] = '\0';
//         strcat(new_str, first_point + rep_len);

//         free(strr);
//         strr = strdup(new_str);
//         first_point = strstr(strr, substrr);

//         free(new_str);
//     }

//     return strr;

// }

int check_str(char* st1, char* ker, int ker_size) {
    int l1 = strlen(st1), l2 = strlen(ker);
    if (l1%l2!=0) {return 0;}
    for(int i = 0; i<l1/l2;i++) {
        // printf("%d\n", i);
        if (strncmp(st1+(i*(ker_size)), ker, ker_size) != 0) {
            return 0;
        }
    }
    
    return 1;

}

char * gcdOfStrings(char * str1, char * str2){
    
    int l1 = strlen(str1), l2 = strlen(str2);
    char* small = l1>=l2?strdup(str2):strdup(str1);
    char* big = l1<l2?strdup(str2):strdup(str1);

    int ls = strlen(small), lb = strlen(big), i = 0, kernel_size = ls;
    while (kernel_size > 0) {
        while (i<ls-kernel_size+1) {
            char* kernel = (char*)calloc(kernel_size+1, sizeof('a'));
            strncpy(kernel, i + small, kernel_size);
            // printf("%s\n", kernel);
            if (check_str(big, kernel, kernel_size) && check_str(small, kernel, kernel_size) ) {
                return kernel;
            }
            free(kernel);
            i++;
        }
        kernel_size--;
    }
    char* kernel = "";
    return kernel;
}
