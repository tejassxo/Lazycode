class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 0

        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            curr_len = right - left - 1
            if curr_len > max_len:
                start = left + 1
                max_len = curr_len

            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            curr_len = right - left - 1
            if curr_len > max_len:
                start = left + 1
                max_len = curr_len

        result = s[start:start + max_len]
        return result
                