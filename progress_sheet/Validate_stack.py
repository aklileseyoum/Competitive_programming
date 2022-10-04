class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        s = []
        j = 0
        for i in pushed:
            s.append(i)
            while s and popped[j] == s[-1]:
                s.pop()
                j = j + 1
                
        if not s:
            return True
        else:
            return False
