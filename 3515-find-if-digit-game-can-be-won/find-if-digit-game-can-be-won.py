class Solution(object):
    def canAliceWin(self, nums):
        single=0
        double=0
        for i in nums:
            if 10<=i<=99:
                double+=i
            else:
                single+=i
        return double!=single
        