class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(num) < 3:
            return[]
        
        nums = sorted(nums)

        solutions = []