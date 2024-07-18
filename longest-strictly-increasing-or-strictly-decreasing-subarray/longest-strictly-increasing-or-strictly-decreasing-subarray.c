int longestMonotonicSubarray(int* nums, int numsSize) {
    if (!numsSize)
        return 0;
    int il=1, dl=1, iil=1, idl=1,i=0, j=1;
    // increasing
    while(i<numsSize){
        j = i+1;
        iil=1;
        while(j < numsSize){
            if (!( nums[j]>nums[j-1])){
                break;
            }
            iil++;
            j++;
        }
        i++;
        il = iil>il?iil:il;
    }
    i = 0;
    // decreasing
    while(i<numsSize){
        j = i+1;
        idl=1;
        while(j<numsSize){
            if(!(nums[j]<nums[j-1]))
                break;
            idl++;
            j++;
        }
        i++;
        dl = idl>dl?idl:dl;
    }
            
    return il>=dl?il:dl;
}
