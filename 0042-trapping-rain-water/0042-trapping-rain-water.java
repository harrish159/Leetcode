class Solution {
    public int trap(int[] height) {
        int start=0;
        int end=height.length - 1;
        int leftmax=0;
        int rightmax=0;
        int trap=0;

        while(start<=end)
        {
            if(height[start]<=height[end])
            {
                if(leftmax<height[start])
                    leftmax=height[start];
                else
                    trap = trap+leftmax-height[start];

                start++;
            }

            else
            {
                if(rightmax<height[end])
                    rightmax=height[end];
                else
                    trap=trap+rightmax-height[end];

                end--;
            }
        }
        return trap;
    }
}