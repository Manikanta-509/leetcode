class Solution(object):
    def singleNumber(self, nums):
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for val in freq:
            if freq[val]==1:
                return val
        """
        :type nums: List[int]
        :rtype: int
        """
        