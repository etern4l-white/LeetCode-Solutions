int sumIndicesWithKSetBits(int* nums, int numsSize, int k){
  int s = 0, c;
  for (int i = 0; i<numsSize;i++){
    c = 0;
    for(int j = 0; j<10;j++){
      c+= (i&(1<<j)) != 0;
    }
    if (c==k){
      s+=nums[i];
    }
  }
  return s;
}
