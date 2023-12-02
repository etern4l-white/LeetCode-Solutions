bool uniqueOccurrences(int* arr, int arrSize) {
	int arr1[2001], arr2[2001];
	for(int i = 0;i<2001;i++) {
		arr1[i] = 0;
		arr2[i] = 0;
	}
	for(int i = 0;i<arrSize;i++) {
		arr1[arr[i]+1000]++;
	}
	for(int i = 0;i<2001;i++) {
		arr2[arr1[i]]+=arr1[i]!=0;
	}
	/*	
	for(int i = 0;i<2001;i++) {
		printf("%d ", arr1[i]);
	}
	printf("\n");
	for(int i = 0;i<2001;i++) {
		printf("%d ", arr2[i]);
	}
	printf("\n");
	*/
	for(int i = 0;i<2001;i++) {
		if (arr2[i] > 1) {
			return 0;
		}
	}
	return 1;
}
