"""
Good Solution:
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}#字典key为字符串值，value为出现的位置
        for i, c in enumerate(s):#i为位置，c为字符串值
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前子串的起始下标k
                k = c_dict[c] #当前子串的起始下标更新  
				#c_dict[c] = i
            else:
				#c_dict[c] = i
                res = max(res, i-k)
			c_dict[c] = i#更新字符串值c的位置，这句话相当于被注释掉的两句话
        return res