/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int* nums2 = (int*)malloc(numsSize*2*sizeof(int));
    for(int i=0;i<numsSize;i++){
        nums2[i] = nums[i];
    }
    for(int i=0;i<numsSize;i++){
        nums2[i+numsSize] = nums[i];
    }
    *returnSize = numsSize*2;
    return nums2;
}
