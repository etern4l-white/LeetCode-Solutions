int addDigits(int num) {
    int s = 0, temp = num;
    if (num<10){return num;}
    while(num>=10){
        s = 0;
        temp = num;
        while(temp >= 10){
            s+=temp%10;
            temp/=10;
        }
        s+=temp%10;
        num = s;
        
    }
    return s;
}
