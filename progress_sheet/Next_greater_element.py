class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        a = -1
        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    if j == len(nums2) - 1:
                        a = -1
                    else:
                        b = nums2[j]
                        for k in range(j, len(nums2)):
                            if b < nums2[k]:
                                a = nums2[k]
                                break
                            else:
                                a = -1
                    ans.append(a)
                    
        return ans
