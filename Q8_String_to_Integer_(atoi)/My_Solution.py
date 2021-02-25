"""
My answer:
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        else:
            longest_length = 0
            first_pointer = 0
            last_pointer = 1
            moved_flag = False
            while last_pointer<len(s):#直到尾指针到字符串末尾
                moved_flag = False
                length = 1
                for i in range(first_pointer,last_pointer): 
                    if s[i]==s[last_pointer]:
                        first_pointer+=1
                        moved_flag = True #一次只移动头指针(当前字符串子串中有重复字符)或者尾指针(当前字符串子串中没有重复子串）
                        break
                    else:
                        length+=1
                        pass
                if moved_flag ==False:
                    last_pointer+=1
                if length>longest_length:
                    longest_length=length #记录最长的无重复字符串长度
            return longest_length                    
            