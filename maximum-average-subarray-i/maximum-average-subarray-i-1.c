#include <limits.h>
double avg(int* arr, int start, int finish){
    int s = 0, l = finish-start;
    for(int x= start;x<finish;x++){
        s+=arr[x];
    }
    return (double)s/l;
}


double findMaxAverage(int* nums, int numsSize, int k){
    double a = INT_MIN, c, s = 0;
    if (numsSize <=k){
        return avg(nums, 0, numsSize);
    }
    for(int i = 0; i<k;i++) {
        s+=nums[i];
    }
    a = (double)s/k;
    for(int i =0;i<numsSize-k;i++){
        s-=nums[i];
        s+=nums[k+i];
        c=(double)s/k;
        a=c>a?c:a;
    }

    return a;
}
