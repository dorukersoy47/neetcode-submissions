class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = []
        for i, num in enumerate(nums):
            L.append([num, i])
        L.sort()

        i, j = 0, len(nums) - 1

        while i < j:
            curr = L[i][0] + L[j][0]
            if curr == target:
                return [min(L[i][1], L[j][1]), max(L[i][1], L[j][1])]
            elif curr < target:
                i += 1 # if the total sum is lower than target then increase
            else:
                j -= 1 # if the total sum is higher than target then decrease
        return []