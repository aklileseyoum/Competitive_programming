class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        a = 0
        b = 1
        i = 1
        while i < n:
            c = a + b
            a = b
            b = c
            i += 1
            
        return c
