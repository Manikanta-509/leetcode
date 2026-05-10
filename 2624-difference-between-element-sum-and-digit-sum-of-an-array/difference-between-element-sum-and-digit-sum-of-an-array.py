class Solution(object):
    def differenceOfSum(self, nums):
        total=sum(nums)
        digits=0
        for num in nums:
            while num>0:
                digits+=num%10
                num=num//10
        return total-digits
        
        