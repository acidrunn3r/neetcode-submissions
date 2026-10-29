class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            halfIndex = int((left + right) / 2)

            if nums[halfIndex] == target:
                return halfIndex

            if nums[halfIndex] > target:
                right = halfIndex - 1
            else:
                left = halfIndex + 1

        return -1
            