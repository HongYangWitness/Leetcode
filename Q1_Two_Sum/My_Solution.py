"""
My answer:
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target-nums[i] in nums): #寻找target减去当前数组元素的值是否在数组中
                if nums.index(target-nums[i])!=i:#因为每个数组元素只能用一次，所以index不能为i本身
                    return[i,nums.index(target-nums[i])]
            else:
                pass      
        return 0