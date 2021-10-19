# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.

def stray(arr):
    return min(set(arr), key=arr.count)


# Create a function to determine whether or not two circles are colliding. You will be given the position of both circles in addition to their radii:

import math
def collision(x1, y1, radius1, x2, y2, radius2): 
    return radius1 + radius2 >= math.dist((x1, y1), (x2, y2))


#Your task is to get Zodiac Sign using input day and month.

def get_zodiac_sign(day, month):
    if day >= 21 and month == 3:
        return "Aries"
    elif day < 20 and month == 4:
        return "Aries"
    elif day >19 and month == 4:
        return "Taurus"
    elif day < 21 and month == 5:
        return "Taurus"
    elif day > 20 and month == 5:
        return "Gemini"
    elif day < 21 and month == 6:
        return "Gemini"
    elif day > 21 and month == 6:
        return "Cancer"
    elif day < 23 and month == 7:
        return "Cancer"
    elif day > 22 and month ==7:
        return "Leo"
    elif day < 23 and month == 8:
        return "Leo"
    elif day > 22 and month == 8:
        return "Virgo"
    elif day < 23 and month == 9:
        return "Virgo"
    elif day > 22 and month == 9:
        return "Libra"
    elif day < 23 and month == 10:
        return "Libra"
    elif day > 22 and month == 10:
        return "Scorpio"
    elif day < 22 and month == 11:
        return "Scorpio"
    elif day > 21 and month == 11:
        return "Sagittarius"
    elif day < 22 and month == 12:
        return "Sagittarius"
    elif day > 21 and month == 12:
        return "Capricorn"
    elif day < 20 and month == 1:
        return "Capricorn"
    elif day > 19 and month == 1:
        return "Aquarius"
    elif day < 19 and month == 2:
        return "Aquarius"
    else:
        return "Pisces"
    
    
# Each time the function is called it should invert the passed triangle. Make upside down the given triangle and invert the chars in the triangle.

def invert_triangle(t):
    return t[::-1].translate(str.maketrans('# ', ' #'))


#######
def reverse_list(x):
    #Takes an list and returns the reverse of it. 
    return x[::-1]

def sum_list(x):
# The sum_list function takes a list as input and adds up all the values, 
# returning an integer. If x is empty list, return 0.
    if x == []:
        return 0
    else:
        return sum(x)

def head_of_list(x):
#Takes a list, returns the first item in that list.
#If x is empty, return None

    if x == []:
        return None
    else:
        return x[0]
