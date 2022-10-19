class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        ans = 0
        
        if len(people) <= 1:
            return 1
        people.sort()
        i = 0
        j = len(people)-1
        while i <= j:
            if people[j] + people[i] <= limit:
                j-=1
                i+=1
            else:
                j-=1
                
            ans += 1
            
        return ans
        
