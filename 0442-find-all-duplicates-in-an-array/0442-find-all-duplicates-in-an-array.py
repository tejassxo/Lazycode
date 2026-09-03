class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        res = []
        for num,count in freq.items():
            if count == 2:
                res.append(num)
        return res  
     
