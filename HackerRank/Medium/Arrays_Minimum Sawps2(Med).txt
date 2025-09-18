#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    i = 0
    while i < len(arr):
        correct_pos = arr[i] - 1
        if arr[i] != arr[correct_pos]:
            arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
            count += 1
        else:
            i += 1
    return count



# range안에 len인지 그게 헷갈림 (while이든 range이든)
# for i in range(len(arr)):   # i = 0,1,2,3 ✅ OK
# while i < len(arr):         # ✅ 마지막은 i == 3까지 OK