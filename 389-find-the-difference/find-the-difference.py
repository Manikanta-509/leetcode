class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq1={}
        freq2={}
        for i in s:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        for i in t:
            if i in freq2:
                freq2[i]+=1
            else:
                freq2[i]=1
        for key in freq2:
            if key not in freq1:
                return key
            elif freq2[key]>freq1[key]:
                return key


            
        