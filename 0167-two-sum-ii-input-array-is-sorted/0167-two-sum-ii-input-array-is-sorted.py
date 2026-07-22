class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        l,r = 0,len(arr)-1
        while l<r:
            c_sum = arr[l] + arr[r]
            if c_sum == target :
                return (l+1,r+1)
            elif c_sum < target :
                l+=1
            else:
                r-=1
        return None
        