class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_table = {}
        
        for i, value_1 in enumerate(nums):
            value_2 = target - value_1
            if value_2 in num_table:
                return [num_table[value_2], i] 
            
            num_table[value_1] = i
