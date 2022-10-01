class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = -1
        for i in range(len(nums)):
            if i == 0:
                summ = sum(nums[1:])
                if summ == 0:
                    a = 0
                    return a
            else:
                sum1 = sum(nums[:i])

                j = i + 1
                sum2 = sum(nums[j:])
    
                if sum1 == sum2:
                    a = i
                    break
                else:
                    continue
                
        return a
