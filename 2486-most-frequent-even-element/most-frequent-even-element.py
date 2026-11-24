class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        freq={}
        max1=0
        ano=-1
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        b=False
        for key,value in freq.items():
            if key%2==0 and value>max1:
                max1=value
                ano=key
            elif key%2==0 and max1==value and key<ano:
                ano=key
        return ano