/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findArray(int* pref, int prefSize, int* returnSize) {
    // int *returnArr=malloc(prefSize * sizeof(int));
    *returnSize=prefSize; //WHY
    int* hi = (int*)malloc(prefSize * sizeof(int));
    int last_xor, temp;
    for (int i = 0;i<prefSize;i++){
        hi[i] = pref[i];
    }
    last_xor = hi[0];
    for(int i = 1;i<prefSize;i++) {
        temp = hi[i];
        hi[i]^=last_xor;
        last_xor=temp;
    }

    // for (int i = 0;i<prefSize;i++){
    //     returnSize[i] = hi[i];
    // }

    // return returnSize;
    return hi;


}
