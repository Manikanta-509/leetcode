class Solution(object):
    def removeDuplicates(self, nums):
        left=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[left]:
                left+=1
                nums[left]=nums[i]
        return left+1
        """
        :type nums: List[int]
        :rtype: int
        """
        