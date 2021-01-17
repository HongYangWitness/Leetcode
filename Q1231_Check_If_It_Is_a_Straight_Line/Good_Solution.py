"""
Good Solution:
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        dit = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result=0
        result =result +dit[s[0]]
        for i in range(1,len(s)):#从第二个字母开始遍历
            result=result+ dit[s[i]]
            if dit[s[i]]>dit[s[i-1]]:#如果当前字母的值比前一个大（对应特殊情况）
                result = result- 2*dit[s[i-1]] #IV顺序算应该是6，但其实应该是4，所以减去2*1
        return result
        