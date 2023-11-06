int commonFactors(int a, int b) {
    int m = a>b?a:b, n = a<b?a:b;
    int sum = 0;
    for(int i = 2; i<=n;i++) {
        if (n%i==0 && m%i==0){
            sum++;
            // n/=i;
            // i-=1;
        }
    }
    return 1+sum;
}
