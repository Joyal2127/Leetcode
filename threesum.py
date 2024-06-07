class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return[]
        
        nums = sorted(nums)

        solutions = []

        for i in range(len(nums)- 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i+1
            k = len(nums)-1
            target = -nums[i]

            while j < k:
                jksum = nums[j] + nums[k]

                if jksum == target:
                    solutions.append([nums[i], nums[j], nums[k]])

                    j =+ 1
                    k -= 1

                    while j < k and nums[j] == [j- 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k =- 1
                elif jksum < target:
                    j += 1 
                else:
                    k -= 1
        return solutions

