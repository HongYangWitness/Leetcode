"""
My answer:
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return[]
        elif numRows==1:
            return [[1]]
        elif numRows ==2:
            return [[1],[1,1]]
        else:
            square = [[1],[1,1]]
            for i in range(2,numRows):
                row = [1]#第一个数加1
                for j in range(len(square[i-1])-1):
                    row.append(square[i-1][j]+square[i-1][j+1])#定义
                row.append(1)#末尾加1
                square.append(row)
            return square