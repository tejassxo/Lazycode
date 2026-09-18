class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        freq = {}
        n = len(nums)
        for i in nums:
            freq[i] = freq.get(i,0)+1
        res = []
        for i in freq:
            if freq[i]>n//3:
                res.append(i)
        return res