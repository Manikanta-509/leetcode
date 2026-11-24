class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for value in freq.values():
            if value>=2:
                return True
        return False
        
        