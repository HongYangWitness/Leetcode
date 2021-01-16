"""
Good Solution:
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0) or ((x!=0) and (x%10==0)): #小于0和0结尾的肯定不是
            return False
        else:
            rev = 0 #反转后半边
            while(x>rev):#如果x小于rev说明已经过半
                last = x%10
                rev = rev*10+ last
                x = x//10
            return x == rev or x == rev // 10; #对于偶数位 x== rev 对于奇数位x== rev//10（会多中间一位）;