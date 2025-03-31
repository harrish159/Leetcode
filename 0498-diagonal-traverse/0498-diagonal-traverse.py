class Solution(object):
    def findDiagonalOrder(self, mat):
        flag=1
        n=len(mat)
        m=len(mat[0])
        length=len(mat)*len(mat[0])
        result = []
        row,col=0,0
        for i in range(0,length):
            result.append(mat[row][col])
            if(flag):
                if col==m-1:
                    row+=1
                    flag=0

                elif row==0:
                    col+=1
                    flag=0 
                else:
                    row-=1
                    col+=1

            else:
                if row==n-1:
                    col+=1
                    flag=1
                elif col==0:
                    row+=1
                    flag=1
                else:
                    row+=1
                    col-=1     
        return result
                
