class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        original=x
        total=0
        while x>0:
            digit=x%10
            total+=digit
            x//=10
        if original%total==0:
            return total
        return -1
        