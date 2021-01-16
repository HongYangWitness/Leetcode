"""
My answer:
"""
class Solution:
    def reverse(self, x: int) -> int: #思路转换成String进行反转，最后转换成int，如果是负数加负号
        negative = False
        x_output = 0
        if (x<0):#如果是负数
            negative = True
            x= abs(x)
        x_string = str(x)
        x_string_output = ''
        for i in range(len(x_string)-1,-1,-1):
            x_string_output += x_string[i] #反转的输出的string
        if negative : 
            x_output = int(x_string_output)*-1#小于0 加负号
        else:
            x_output = int(x_string_output)
        if (x_output>pow(2,31)-1) or (x_output<-pow(2,31)): #如果输出超出范围则输出0
            return 0
        else:
            return x_output