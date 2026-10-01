class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = float('inf')
        n = len(nums)
        curr_sum = 0
        start = 0 
        for end in range(n):
            curr_sum += nums[end]
            while curr_sum>=target:
                min_len = min(min_len,end-start+1)
                curr_sum -= nums[start]
                start+=1
        return 0 if min_len == float('inf') else min_len