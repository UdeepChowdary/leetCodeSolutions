class Solution {
    public int majorityElement(int[] nums) {
        int majNum = 0;
        int count = 0;

        for (int i = 0; i < nums.length; i++) {
            if (count == 0) {
                majNum = nums[i];
            }
            if (nums[i] == majNum) {
                count++;
            } else {
                count--;
            }
        }
        return majNum;
    }
}