"""
My answer:
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x<10:
            return True
        else:
            for i in range(len(str(x))//2):
                last = x %pow(10,i+1)//pow(10,i) #倒数第i+1位
                if i==0:
                    first = x//pow(10,len(str(x))-i-1)  #正数第i+1位
                else :
                     first = x//pow(10,len(str(x))-i-1) %10
                if (first !=last):
                    return False
            return True