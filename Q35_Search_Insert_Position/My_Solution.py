"""
My answer:
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0]>target: #插入位置为0
            return 0
        for i in range(0,len(nums)-1):
            if nums[i]==target:#找到了索引位置
                return i
            elif (nums[i]<target) and (nums[i+1]>target):#找到插入位置
                return i+1
        if nums[len(nums)-1]==target: #找到了位置在最后一个
            return len(nums)-1
        return len(nums) #插入位置在最后一个后面