class Solution {
    public int maxArea(int[] height) {
        int start=0;
        int end=height.length-1;
        int max=0;
        while(start<=end)
        {
            int widhth = end - start;
            int l = Math.min(height[start],height[end]);
            int area = widhth * l;
            max = Math.max(area,max);
            if(height[start]<height[end])
                start++;
            else 
                end--;
        }
        return max;
    }
}