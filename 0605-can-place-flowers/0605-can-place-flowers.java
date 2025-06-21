class Solution 
{
    public boolean canPlaceFlowers(int[] arr, int n) 
    {
        if(n==0) return true;
        int len = arr.length;
        for(int i=0;i<len;i++)
        {
            if(arr[i]==0 && (i==len-1 || arr[i+1]==0) && (i==0 || arr[i-1]==0))
            {
                n--;
                arr[i]=1;
            }
            if(n==0) return true;
        }
         return false;
    }
}