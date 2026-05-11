class Solution(object):
    def maximumWealth(self, accounts):
        richest=0
        for cus in accounts:
            wel=sum(cus)
            if wel>richest:
                richest=wel
        return richest

        