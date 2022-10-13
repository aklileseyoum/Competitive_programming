class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = []
        sub_string=[]
        for i in range(len(s)):
            if i == 0:
                sub_string.append(s[i])
            else:
                if s[i] in sub_string:
                    ans.append(len(sub_string))
                    j = sub_string.index(s[i])
                    sub_string = sub_string[j+1:]
                sub_string.append(s[i])
               
        ans.append(len(sub_string))
        if not ans:
            return 0
        result = max(ans)
        
        return result
