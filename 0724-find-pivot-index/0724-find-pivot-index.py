class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        l= 0
        for i in range(n):
            r = total - l - nums[i]
            if l == r:
                return i
            l += nums[i]
        return -1
        # n = len(nums)
        # sum_lef = []
        # sum_rig= []
        # for i in range(0,n):
        #     sum_lef.append(nums[i])
        #     sum_rig.append(nums[n-i-1])
        #     if sum_lef[i]==sum_rig[i]:
        #         return i
        #     else:
        #         return -1

        