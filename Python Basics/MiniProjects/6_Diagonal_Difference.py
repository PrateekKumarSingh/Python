#!/bin/python3
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    size = len(arr[0]) - 1 
    print('size:',size)
    lrd = rld = 0
    for i in range(0,size+1):
            print('arr[{0}][{1}]={2}'.format(i,i,arr[i][i]))
            lrd += arr[i][i]
            x=size-i
            print('arr[{0}][{1}]={2}'.format(i,x,arr[i][x]))
            rld += arr[i][(size-i)]
    print('rld',rld)    
    print('lrd',lrd)    
    return abs(lrd-rld)

arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]

print(diagonalDifference(arr))