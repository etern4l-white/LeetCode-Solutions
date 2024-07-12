int scoreOfString(char* s) {
    int sum = 0, curr_num = s[0], i = 1;
    while (s[i] != '\0'){
        sum+=curr_num>=s[i]?curr_num-s[i]:s[i]-curr_num;
        curr_num=s[i];
        i++;
    }
    return sum;

}
