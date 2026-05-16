class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        total=sum(nums)
        missing=(n*(n+1))//2
        return missing-total
        """
        :type nums: List[int]
        :rtype: int
        """
        