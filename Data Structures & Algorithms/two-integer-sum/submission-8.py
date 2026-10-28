class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for value_1 in nums:
            value_2 = target - value_1

            print(value_1, value_2)

            if value_2 in nums:
                i = nums.index(value_1)

                try:
                    if value_1 == value_2:
                        j = nums.index(value_2, i + 1)
                    else:
                        j = nums.index(value_2)
                    break
                except ValueError:
                    pass
        
        return [i, j]
            