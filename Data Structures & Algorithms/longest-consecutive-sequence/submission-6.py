class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nnums = sorted(list(set(nums)))
        print(nnums)

        long = 1
        curr = 1

        for i in range(1, len(nnums)):
            if nnums[i] == nnums[i - 1] + 1:
                curr += 1
            else:
                if long < curr:
                    long = curr
                    curr = 1
                else:
                    curr = 1
        
        return max(long, curr)
                
                
