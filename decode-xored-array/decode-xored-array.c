/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decode(int* encoded, int encodedSize, int first, int* returnSize) {
    int* hi = (int*)malloc((encodedSize+1)*sizeof(int));
    *returnSize = encodedSize + 1;
    hi[0] = first;
    for(int i = 1;i<encodedSize+1;i++){
        hi[i] = encoded[i-1]^hi[i-1];
    }
    return hi;

}
