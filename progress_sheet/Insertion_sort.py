#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] < key:
                break
            if arr[j] > key:
                arr[j+1] = arr[j]
                for i in arr:
                    print(i, end=' ')
                print()
            j = j - 1
        arr[j+1] = key
        
    for i in arr:
        print(i, end=' ')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
