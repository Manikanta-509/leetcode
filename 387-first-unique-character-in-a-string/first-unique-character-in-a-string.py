class Solution(object):
    def firstUniqChar(self, s):
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for index,char in enumerate(s):
            if freq[char]==1:
                return index
        return -1
        
        