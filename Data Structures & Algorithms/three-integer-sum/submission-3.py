class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sn = sorted(nums)
        res = []

        for idx in range(len(sn)):
            if idx > 0 and sn[idx] == sn[idx - 1]:
                continue

            i, j = idx + 1, len(sn) - 1

            while (i < j):
                val = sn[idx] + sn[i] + sn[j]
                if val == 0:
                    res.append([sn[idx], sn[i], sn[j]])
                    i += 1
                    j -= 1
                    while i < j and sn[i] == sn[i - 1]:
                        i += 1
                    while i < j and sn[j] == sn[j + 1]:
                        j -= 1
                elif val < 0:
                    i += 1
                else:
                    j -= 1
        
        return res