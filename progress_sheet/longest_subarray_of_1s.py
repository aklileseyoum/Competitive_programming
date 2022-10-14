class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        ones = []
        for i in nums:
            if i == 1:
                ones.append(i)
            else:
                if ones and 0 in ones:
                    ans.append(len(ones)-1)
                    j = ones.index(0)
                    ones = ones[j+1:]
                ones.append(i)
                
        ans.append(len(ones)-1)
        result = max(ans)
        return result
