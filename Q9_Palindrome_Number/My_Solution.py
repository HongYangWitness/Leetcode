"""
My answer:
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s =="":
            return True
        transfer_s =[]
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                transfer_s.append(s[i].lower())
            else:
                pass
        last_half = []
        for i in range(len(transfer_s)//2):
            last_half.append(transfer_s[len(transfer_s)-1-i])#这里将后半边翻转与前半边比较
            #if transfer_s[len(transfer_s)-1-i] != transfer_s[i]:#注释掉的是直接前半边和后半边对称位置一一比较
            #    return False
        if last_half!= transfer_s[0:len(transfer_s)//2]:
            return False
        else:
            return True
        #return True