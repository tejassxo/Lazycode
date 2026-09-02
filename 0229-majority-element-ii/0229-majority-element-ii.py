class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # result = []
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] in result:
        #         continue
        #     count = 0
        #     for j in range(n):
        #         if nums[j] == nums[i]:
        #             count += 1
        #     if count > n // 3:
        #         result.append(nums[i])
        # return result
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        res=[]
        for num in freq:
            if freq[num]>len(nums)//3:
                res.append(num)
        return res
