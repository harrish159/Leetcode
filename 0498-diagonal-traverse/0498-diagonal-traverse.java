class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;
        int[] result = new int[n * m];

        int row = 0, col = 0, idx = 0;
        boolean flag = true;

        while (idx < n * m) {
            result[idx++] = mat[row][col];

            if (flag) 
            {
                if (col == m - 1) 
                {
                    row++;
                    flag = false;
                } 
                else if (row == 0) 
                {
                    col++;
                    flag = false;
                } 
                else
                {
                    row--;
                    col++;
                }
            } 
            else 
            { 
                if (row == n - 1) 
                {
                    col++;
                    flag = true;
                } 
                else if (col == 0)
                {
                    row++;
                    flag = true;
                } else 
                {
                    row++;
                    col--;
                }
            }
        }

        return result;
    }
}
