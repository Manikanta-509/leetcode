class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        freq1={}
        for i in nums:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        for key,value in freq1.items():
            if value>1:
                return key
        