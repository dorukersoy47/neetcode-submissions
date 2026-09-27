from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(0, len(nums)):
            prefix[i] = nums[0] if i == 0 else nums[i] * prefix[i - 1]
            postfix[len(nums) - i - 1] = nums[len(nums) - 1] if i == 0 else nums[len(nums) - i - 1] * postfix[len(nums) - i]
        
        for i in range(0, len(nums)):
            pre = 1 if i == 0 else prefix[i - 1]
            post = 1 if i == len(nums) - 1 else postfix[i + 1]
            output[i] = pre * post
        
        return output