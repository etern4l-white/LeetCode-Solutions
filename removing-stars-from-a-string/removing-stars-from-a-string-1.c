char* removeStars(char* s) {
    int len = 0, nos = 0, i = 0, c = 0;
    while(s[i]!='\0'){
        len++;
        i++;
    }

    i = 0;
    char stack[len+1];
    while(s[i] != '\0'){
        if (s[i] != '*'){
            stack[c] = s[i];
            c++;
        } else {
            c--;
            stack[c] = '\0';
            
        }
        i++;
    }
    stack[c] = '\0';
    i = 0;
    while(stack[i] != '\0'){
        s[i] = stack[i];
        i++;
    }
    s[i] = '\0';
    return s;
}
