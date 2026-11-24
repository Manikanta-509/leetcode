class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        l=[]
        for key,value in freq.items():
            if value>=2:
                l.append(key)
        return l
        