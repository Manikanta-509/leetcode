class Solution(object):
    def sortedSquares(self, nums):
        result = []
        
        for i in range(len(nums)):
            result.append(nums[i] * nums[i])
        
        result.sort()
        
        return result
        