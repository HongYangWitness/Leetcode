"""
My answer:
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":#不是空格继续遍历，length+1
                length+=1
            elif s[i]==" " and length == 0:#过滤刚开始的无意义空格，如“a           "
                pass
            else:
                return length #遇见空格停止遍历
        return length #遍历完整个字符串也没发现空格，则整个字符串长度为最后一个单词长度