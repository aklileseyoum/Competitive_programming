class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mx = 3**19
        
        return n>0 and mx%n == 0 
