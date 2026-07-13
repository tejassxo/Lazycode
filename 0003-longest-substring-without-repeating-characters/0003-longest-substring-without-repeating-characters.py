class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res ,m = "", 0
        for char in s:
            if char not in res:
                res += char
            else:
                m = max(m, len(res))
                res = res[res.index(char) + 1:] + char
        return max(m, len(res))
        