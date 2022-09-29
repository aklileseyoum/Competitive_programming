class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=[]
        for i in range(len(nums)):
            k = 0
            for j in nums:
                if nums[i] > j:
                    k = k + 1
            c.append(k)
        return(c)
        
