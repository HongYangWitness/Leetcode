"""
My answer:
"""
class Solution:
    def isValid(self, s: str) -> bool:#匹配时每次遇见一个右括号，必须和左括号栈顶元素匹配（两个在list同一位置）
        left_list = ['(','{','[']
        right_list = [')','}',']']
        left_stack = []
        #right_stack = []
        for i in range(len(s)):
            if s[i] in left_list :
                left_stack.append(s[i])
            else:
                if len(left_stack)==0:#如果右括号比左括号多
                    return False
                elif left_list[right_list.index(s[i])]!=left_stack[-1]  :#右括号和左括号栈顶元素不匹配
                    return False
                else:
                    left_stack = left_stack[0:-1] #出栈
        if len(left_stack)!=0: #如果左括号比右括号多
            return False
        else:
            return True