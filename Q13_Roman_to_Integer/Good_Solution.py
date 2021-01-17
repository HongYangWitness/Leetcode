"""
Good Solution:
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(1,len(coordinates)-1):
            if((coordinates[i][0] - coordinates[i - 1][0]) * (coordinates[i + 1][1] - coordinates[i][1]))!= ((coordinates[i][1] - coordinates[i - 1][1]) * (coordinates[i + 1][0] - coordinates[i][0])):
                return False
        return True
