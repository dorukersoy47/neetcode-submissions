class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have two pointer i and j
        # one of them moves as the other one finishes
        # the time complexity is O(n^2) which is not efficient at all
        # but let's solve it this way first

        res = []

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []