class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        total=0
        c=0
        for key,value in freq.items():
            if value%2==0:
                total+=value
            elif value%2!=0:
                total+=(value-1)
                c+=1
        if c>=1:
            total+=1
        return total
            


        