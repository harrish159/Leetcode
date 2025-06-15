class Solution {
    public int removeDuplicates(int[] nums) {
        int start=0,end=1;
        int len = nums.length;
        int count=0;
        while(end<len)
        {
            if(nums[start]!=nums[end])
            {
                start++;
                nums[start]=nums[end];
            }
            end+=1;
        }
        return start+1;
    }
    
}