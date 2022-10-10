class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips.sort(key = lambda t: t[1])
        
        minHeap = []
        curPas = 0
        for t in trips:
            numPass, start,end = t
            while minHeap and minHeap[0][0] <= start:
                curPas -= minHeap[0][1]
                heapq.heappop(minHeap)
            curPas += numPass
            if curPas > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
            
        return True
