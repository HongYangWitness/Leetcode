"""
My answer:
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:    
        replace_index = 1 #从第二个数开始替换
        if len(nums)==1 or len(nums)==0:
            return len(nums)
        duplicate = nums[0]
        i=1
        while i<len(nums):
            if nums[i]== duplicate:#如果是重复的数字，则继续遍历下一个
                i=i+1
            else:
                duplicate = nums[i]#当前不重复的值在替换到replace_index后则为重复的了，所以要更新duplicate值
                nums[replace_index]=nums[i] #替换位换成目前不重复的那个值
                replace_index +=1#替换位置后移一位
        return replace_index