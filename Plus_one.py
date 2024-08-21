from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit and move towards the first digit
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                # If the current digit is less than 9, just increment it by 1
                digits[i] += 1
                return digits
            else:
                # If the current digit is 9, set it to 0
                digits[i] = 0
        
        # If all the digits were 9, then we need to add a new digit at the front
        return [1] + digits
