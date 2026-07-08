class Solution {
    public boolean isPalindrome(int x) {
        int temp = x;
        int lastDigit = 0;
        int revNum = 0;
        while(temp>0){
            lastDigit = temp%10;
            revNum = (revNum*10)+lastDigit;
            temp/=10;
        }
        if(x==revNum){
            return true;
        }else{
            return false;
        }
    }
}