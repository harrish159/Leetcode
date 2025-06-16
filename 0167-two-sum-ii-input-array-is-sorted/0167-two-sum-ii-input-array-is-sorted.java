class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int start=0,end=numbers.length - 1;
        int res[] = new int[2];
        int sum=0;
        while(start<end)
        {
            sum = numbers[start] + numbers[end];
            if(sum==target)
            {
                res[0]=start+1;
                res[1]=end+1;
                return res;
            }
            else if(sum>target)
            {
                end--;
            }
            else{
                start++;
            }
        }
        return new int[0];
    }
}