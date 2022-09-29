#User function Template for python3

class Solution: 
    #def select(self, arr, i):
        # code here 
    
    def selectionSort(self, arr,n):
        #code here
        for j in range(n):
            k = 0
            mini = arr[j]
            for i in range(j+1, n):
                if arr[i] < mini:
                    mini = arr[i]
                    a = i
                    k = 1
            if k ==1:
                temp = arr[j]
                arr[j] = mini
                arr[a] = temp
