class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        longest=0
        count=0
        for i in nums:
            if i==1:
                count+=1
                longest=max(longest,count)
            else:
                count=0
        return longest
        """
        :type nums: List[int]
        :rtype: int
        """
        