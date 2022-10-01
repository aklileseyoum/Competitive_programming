class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = []
        for i in s:
            if s1:
                top = s1[-1]
            if i == '(' or i == '{' or i == '[':
                s1.append(i)
            elif i == ')':
                if not s1 or top != '(':
                    return False
                else:
                    s1.pop()
            elif i == ']':
                if not s1 or top != '[':
                    return False
                else:
                    s1.pop()
            elif i == '}':
                if not s1 or top != '{':
                    return False
                else: 
                    s1.pop()
        
        if not s1:
            return True
        else: 
            return False
            
        
