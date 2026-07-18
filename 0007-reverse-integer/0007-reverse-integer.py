class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647
        result = 0
        is_negative = x < 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x = x // 10
            
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                result = 0
                break
                
            result = (result * 10) + digit

        if is_negative and result != 0:
            result = -result

        return result
                