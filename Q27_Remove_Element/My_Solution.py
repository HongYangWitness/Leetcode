"""
My answer:
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return len(nums)
        for i in range(len(nums)-1,-1,-1):#倒着遍历
            if nums[i]==val:
                nums.pop(i)#发现与val相等就弹出
        return len(nums)