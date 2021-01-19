"""
My answer:
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int: 
        length = len(needle)
        if length==0: #空字符串
            return 0
        for i in range(len(haystack)):
            if haystack[i]==needle[0]: #如果haystack[i]为匹配字符串的第一个字母，我们查看haystack[i:len(needle)]是否等于needle
                if i+length>len(haystack):#长度已经超出haystack，证明长度与needle长度不一样那直接pass不用看。
                    pass
                else:
                    end_index = i+length
                    if haystack[i:end_index]==needle:
                        return i
                    else:
                        pass
        return -1