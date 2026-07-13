class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,h = 0,n-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                l = mid+1
            else:
                h = mid-1
        return -1