"""
Good Solution:
"""
class Solution:
    def reverse(self, x: int) -> int: #直接用数字来计算
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1<<31) -1 if x>0 else 1<<31
        while y != 0:
            res = res*10 +y%10 #反转的第i位等于原来倒数第i位
            if res > boundry :#转换过程中检查，如果已经大于则不必要继续
                return 0
            y //=10
        return res if x >0 else -res #负数加负号