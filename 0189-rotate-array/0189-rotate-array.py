class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        if k > 0:
            nums[:] = nums[-k:] + nums[:-k]
        