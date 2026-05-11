class Solution(object):
    def differenceOfSums(self, n, m):
        divi_n=0
        for i in range(1,n+1):
            if i%m!=0:
                divi_n+=i
        divi_m=0
        for i in range(1,n+1):
            if i%m==0:
                divi_m+=i
        return divi_n-divi_m
        