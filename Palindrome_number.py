class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        n = str(x)
        # Reverse the string and compare it to the original string
        return n == n[::-1]