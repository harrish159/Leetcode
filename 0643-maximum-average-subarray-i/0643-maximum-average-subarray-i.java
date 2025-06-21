class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sum=0;
        int start=0;
        int end=k;
        double avg=0;
        double max=0;
        for(int i=0;i<k;i++)
            sum+=nums[i];
        avg=(double)sum/k;
        max=avg;
        while(end<nums.length)
        {
            sum=sum-nums[start++];
            sum=sum+nums[end++];
            avg = (double)sum/k;
            max=Math.max(max,avg);
        }
        return max;
    }
}