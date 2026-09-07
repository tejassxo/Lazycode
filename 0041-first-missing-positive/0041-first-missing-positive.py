class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)
        for i in range(1,n+2):
            if i not in nums:
                return i        
        # for i in range(n):
        #     while 1 <= nums[i]<= n and nums[nums[i]-1]!= nums[i]:
        #         ind = nums[i]-1
        #         nums[i],nums[ind]=nums[ind],nums[i]
        # for i in range(n):
        #     if nums[i] != i+1:
        #         return i+1
        # return n+1
        