class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        result=[]
        for key in freq:
            if freq[key]>len(nums)/3:
                result.append(key)
        return result
            
        