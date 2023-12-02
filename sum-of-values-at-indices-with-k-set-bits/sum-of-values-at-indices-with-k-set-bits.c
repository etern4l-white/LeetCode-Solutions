int sumIndicesWithKSetBits(int* nums, int numsSize, int k){
  int s = 0;
  for (int i = 0; i<numsSize;i++){
    if (__builtin_popcount(i) == k)
      s+=nums[i];
  }
  return s;
}
