class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        x = 0
        a = []
        summ = 0
        for i in arr:
            summ += i
            a.append(summ)
        
        j = 0
        for i in range(k-1, len(a)):
            if i == k-1:
                average = a[i] / k
            else:
                average = (a[i] - a[j]) / k
                j+=1
            if average >= threshold:
                x+=1
                
        return x
