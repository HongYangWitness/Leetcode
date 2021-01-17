"""
My answer:
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool: #比较coordinates[i]与coordinates[i-1]和coordinates[i-1]与coordinates[i-2]的斜率
        k_before = 0
        k_now = 0
        try:
            k_before = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        except ZeroDivisionError: #如果平行于y轴
            k_before = float('inf')
        if len(coordinates)>2:
            for i in range(2,len(coordinates)):
                try:
                    k_now = (coordinates[i][1]-coordinates[i-1][1])/(coordinates[i][0]-coordinates[i-1][0])
                except ZeroDivisionError:
                    k_now = float('inf')
                if k_now!=k_before:
                    return False
                else:
                    k_before =k_now
        return True
            