class Solution(object):
    def countDigits(self, num):
        original=num
        count=0
        while num>0:
            digits=num%10
            if original%digits==0:
                count+=1
            num=num//10
        return count

        