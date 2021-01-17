"""
My answer:
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roma = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000,'IV':4, 'IX':9,'XL':40,'XC':90, 'CD':400,'CM':900}
        output=0
        i = 0
        length = len(s)
        while i<length: #不能用for循环来改变循环变量，只能用while
            if (i<len(s)-1) and (s[i]+s[i+1] in dict_roma):#优先考虑特殊情况，如IV
                output+=dict_roma.get(s[i]+s[i+1])
                i+=2
            else:
                output+=dict_roma.get(s[i])
                i+=1
        return output