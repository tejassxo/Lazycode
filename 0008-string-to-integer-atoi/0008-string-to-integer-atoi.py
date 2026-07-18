class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        while i < n and s[i] == ' ':
            i += 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        while i < n and '0' <= s[i] <= '9':
            digit = int(s[i])
            
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                result = INT_MAX if sign == 1 else INT_MIN
                sign = 1 
                break
                
            result = (result * 10) + digit
            i += 1

        result = result * sign
        return result
                