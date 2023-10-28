void moveZeroes(int* nums, int numsSize){
    int l[numsSize];
    int i = 0, j = 0;
    while(i<numsSize){
        if (nums[i] != 0) {
            l[j] = nums[i];
            j++;
        }
        i++;
        
    }
    while(j<numsSize){
        l[j] = 0;
        j++;
    }
    i = 0;
    while(i<numsSize){
        nums[i] = l[i];
        i++;
    }

}
