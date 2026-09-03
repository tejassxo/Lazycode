from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = dict(Counter(nums))
        res = []
        # for num in freq.items():
        #     if freq[num].keys() >=2:
        #         res.append(freq[num].values())
        # return res  
        return [num for num, count in freq.items() if count>=2]  
