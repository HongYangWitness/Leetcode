"""
Good Solution:
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        for i in range(len(nums)):
            index.append(i)
        num_dict = dict(zip(nums,index)) #使用字典(类似于哈希表）key为数组元素值，value为其位置值
        for i in range(len(nums)):
            if ((target-nums[i]) in num_dict) and (num_dict.get(target-nums[i])!=i):
                return[i,num_dict.get(target-nums[i])]
        return 0