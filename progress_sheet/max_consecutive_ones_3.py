class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = []
        ones = []
        t = 0
        l = 0
        count = 0
        if k == 0:
            for i in nums:
                if i == 1:
                    l = 1
                    count += 1
                else:
                    if l == 0:
                        continue
                    else:
                        ans.append(count)
                        count = 0
                        
            ans.append(count)
            result = max(ans)
            return result
        for i in nums:
            if i == 1:
                ones.append(i)
            else:
                if t == k:
                    ans.append(len(ones))
                    if 0 in ones:
                        j = ones.index(0)
                        ones = ones[j+1:]
                        t -= 1
                ones.append(i)
                t += 1
                
        ans.append(len(ones))
        result = max(ans)
        
        return result
