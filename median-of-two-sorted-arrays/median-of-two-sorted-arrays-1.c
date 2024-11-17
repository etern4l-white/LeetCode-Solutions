double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int* asd;  
    bool flag1 = false, flag2 = false;  
    asd = malloc(sizeof(int) * (nums1Size + nums2Size));  
    int br1 = 0, br2 = 0;  
    if (nums2Size == 0){
        for(int i = 0;i<nums1Size;i++){
            asd[i] = nums1[i];
        }

    } else if (nums1Size == 0){
        for(int i = 0;i<nums2Size;i++){
            asd[i] = nums2[i];
        }
    }else {
        for (int i = 0; i < (nums1Size + nums2Size); i++) {  
            if (flag1) {  
                asd[i] = nums2[br2];  
                br2++;  
            } else if (flag2) {  
                asd[i] = nums1[br1];  
                br1++;  
            } else if (nums1[br1] >= nums2[br2]) {  //this is line 23 
                asd[i] = nums2[br2];  
                br2++;  
                if (br2 == nums2Size) {  
                    br2--;  
                    flag2 = true;  
                }  
            } else {  
                asd[i] = nums1[br1];  
                br1++;  
                if (br1 == nums1Size) {  
                    br1--;  
                    flag1 = true;  
                }  
            }  
            printf("%d\n", asd[i]);  
        }  
    }

    if ((nums1Size + nums2Size) % 2 == 0) {  
        double a = (asd[(nums1Size + nums2Size) / 2] + asd[(nums1Size + nums2Size) / 2 - 1]);  
        return a / 2;  
    } else {  
        return asd[(nums1Size + nums2Size) / 2];  
    }  
} 
