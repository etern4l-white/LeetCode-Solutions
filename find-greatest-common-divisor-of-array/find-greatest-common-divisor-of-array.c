int gcd(int a, int b){
    return b==0?a:gcd(b, a%b);
}

int findGCD(int* nums, int numsSize) {
    int s = nums[0], b = nums[0];
    for(int i =0;i<numsSize;i++){
        s = nums[i]<s?nums[i]:s;
        b = nums[i]>b?nums[i]:b;
    }
    return gcd(s, b);
}
