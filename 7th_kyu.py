# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.

def stray(arr):
    return min(set(arr), key=arr.count)


# Create a function to determine whether or not two circles are colliding. You will be given the position of both circles in addition to their radii:

import math
def collision(x1, y1, radius1, x2, y2, radius2): 
    return radius1 + radius2 >= math.dist((x1, y1), (x2, y2))
