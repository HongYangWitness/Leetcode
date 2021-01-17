"""
My answer:
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: #以第一个string为模板去匹配字符串数组中后面所有字符串
        if len(strs)==0:
            return ""
        prefix = strs[0]
        i=1
        length =len(strs)
        
        while i<length:
            #print(i)
            prefix_length=len(prefix)
            if strs[i][0:prefix_length]!=prefix:#注意代码准确性，不能写成prefix not in str[i]
                prefix =prefix[0:-1] #前缀减少1
             #   print(prefix)
            else:
                i = i+1 #如果存在就匹配下一个字符串
            if prefix == "":
                return prefix
        return prefix