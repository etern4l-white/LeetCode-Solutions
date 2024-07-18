bool areOccurrencesEqual(char* s) {
    int nums[26] = {0};
    int i = 0, x;
    while(s[i] != '\0'){
        nums[s[i]%97]+=1;
        i++;
    }
    i = 0;
    while(i<26){
        if(nums[i]>0){
            x=nums[i];
            break;
        }
        i++;
    }
    i=0;
    if (x==0){
        return 1;
    }
    while(i<26){
        if (nums[i] != 0 && nums[i] != x)
            return 0;
        i++;
    }
    return 1;
}
