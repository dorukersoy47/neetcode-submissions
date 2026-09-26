class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # my initial idea is to 
        # make a map of key value pairs from the nums array
        # then iterate through that array to see how many of them have k
        d = {}
        res = []

        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        l = list(sorted_d.keys())

        return l[:k]
