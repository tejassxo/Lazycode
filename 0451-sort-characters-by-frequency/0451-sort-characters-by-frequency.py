from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        # freq = {}
        # n = len(s)
        # res = ''
        # for i in s:
        #     if i in freq:
        #         freq[i]+=1
        #     else:
        #         freq[i]=1
        # arr = list(freq.items())
        # for i in range(len(arr)):
        #     for j in range(len(arr)-i-1):
        #         if arr[j][1] < arr[j+1][1]:
        #             arr[j], arr[j+1] = arr[j+1], arr[j]
        # freq = dict(arr)
        # for ch,count in freq.items():
        #     for i in range(count):
        #         res += ch
        # return 
        count=Counter(s)
        result=[]
        for char,freq in count.most_common():
            result.append(char*freq)
        return "".join(result)