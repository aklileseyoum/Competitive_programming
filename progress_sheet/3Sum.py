class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        n = len(arr)
        arr.sort()
        
        for i in range(n):
            seen = defaultdict(int)
            for j in range(i+1, n):
                diff = target - (arr[i] + arr[j])
                if diff in seen:
                    ans += seen[diff]
                seen[arr[j]] += 1
                
        return ans % (10**9+7)
