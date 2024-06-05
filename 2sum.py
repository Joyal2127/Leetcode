class Solution:
    def twoSum(self, nums, target):
        numbs = list(enumerate(nums))
        numbs.sort(key=lambda x: x[1]) 
        l = 0
        r = len(nums) - 1

        while l < r:
            curr = numbs[l][1] + numbs[r][1]

            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else:
                return [numbs [l][0], numbs[r][0]] 

        return [] 