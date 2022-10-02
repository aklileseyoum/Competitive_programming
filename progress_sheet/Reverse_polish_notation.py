import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i == '+' or i == '-' or i == '*' or i == '/':
                x = int(stack[-1])
                stack.pop()
                y = int(stack[-1])
                stack.pop()
                if i == '+':
                    z = x + y
                elif i == '-':
                    z = y - x
                elif i == '*':
                    z = x * y
                else:
                    z = float(y) / float(x)
                    math.ceil(z)
                stack.append(int(z))
            else:
                stack.append(i)
                
        return stack.pop()
