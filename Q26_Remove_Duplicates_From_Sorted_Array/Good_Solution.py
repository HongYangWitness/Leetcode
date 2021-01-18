"""
Good Solution:
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num_index in range(len(nums)-1, 0, -1): #从末尾开始倒着遍历（栈）
            if nums[num_index] == nums[num_index-1]:
                nums.pop(num_index) #遇见重复元素就剔除
        return len(nums)

