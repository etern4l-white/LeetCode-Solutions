bool isPalindrome(char* s) {
    int l = 0, i = 0, i2=0;
    while(s[l]){
        l++;
    }
    char new_s[l];
    while(s[i]){
        if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z') || (s[i] >= '0' && s[i] <= '9')){
            new_s[i2] = s[i]+(s[i]<'a' && s[i] >= 'A'?32:0);
            i2++;
        } 
        i++;
    }
    int left=0, r=i2-1;
    while(r>left){
        if (new_s[left] != new_s[r]) {
            return false;
        }
        r--;
        left++;
    }
    return true;
}
