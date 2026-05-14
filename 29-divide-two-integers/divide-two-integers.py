class Solution(object):
    def divide(self, dividend, divisor):
        result=int(float(dividend)/divisor)

        MAX = 2**31 - 1
        MIN = -2**31

        if result > MAX:
            return MAX

        if result < MIN:
            return MIN

        return result        