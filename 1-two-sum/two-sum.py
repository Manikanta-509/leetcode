class Solution(object):
    def twoSum(self, nums, target):
        freq={}
        for i in range(len(nums)):
            s=target-nums[i]
            if s in freq:
                return [freq[s],i]
            else:
                freq[nums[i]]=i