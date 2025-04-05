class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        rows=0
        col=0
        mat=[]
        num=0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(num)
                num += 1
            mat.append(row)
        
        for i in commands:
            
            if i == 'RIGHT':
                col+=1

            elif i=='LEFT':
                col-=1

            elif i == 'DOWN':
                rows+=1

            elif i == 'UP':
                rows-=1
        return mat[rows][col]
            

