# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its perimeter.

def area_or_perimeter(l , w):
    if l==w:
        return(l*w)
    else: 
        return((l*2)+(w*2))
      

# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.
# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

def update_light(current):
    if current == "green": 
        return "yellow"
    elif current == "yellow": 
        return "red"
    else: 
        return "green"
    
    
    
# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number) :
    if number % 2 == 0:
        return number*8
    else:
        return number*9
    
    
# Write a function that checks if a given string (case insensitive) is a palindrome.
    
    def is_palindrome(s):
    if s.lower() == s[::-1].lower():
        return True
    else:
        return False
    

# You received a whatsup message from an unknown number. Could it be from that girl/boy with a foreign accent you met yesterday evening?
# Write a simple function to check if the string contains the word hallo in different languages.
# These are the languages of the possible people you met the night before:
# hello - english
# ciao - italian
# salut - french
# hallo - german
# hola - spanish
# ahoj - czech republic
# czesc - polish
    
def validate_hello(greetings):
    return any(x in greetings.lower() for x in ['hello','ciao','salut','hallo','hola','ahoj','czesc'])
           
        
# You're at the zoo... all the meerkats look weird. Something has gone terribly wrong - someone has gone and switched their heads and tails around!
# Save the animals by switching them back. You will be given an array which will have three values (tail, body, head). It is your job to re-arrange the array so that the animal is the right way round (head, body, tail).
# Same goes for all the other arrays/lists that you will get in the tests: you have to change the element positions with the same exact logics
    
def fix_the_meerkat(arr):
    arr_new = arr[::-1]
    return arr_new


# It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.
# Return the average of the given array rounded down to its nearest integer.
# The array will never be empty.
    
def get_average(marks):
    import math
    mean = sum(marks) / len(marks)
    return math.floor(mean)


# Philip's just turned four and he wants to know how old he will be in various years in the future such as 2090 or 3044. His parents can't keep up calculating this so they've begged you to help them out by writing a programme that can answer Philip's endless questions.
# Your task is to write a function that takes two parameters: the year of birth and the year to count years in relation to. As Philip is getting more curious every day he may soon want to know how many years it was until he would be born, so your function needs to work with both dates in the future and in the past.
# Provide output in this format: For dates in the future: "You are ... year(s) old." For dates in the past: "You will be born in ... year(s)." If the year of birth equals the year requested return: "You were born this very year!"
# "..." are to be replaced by the number, followed and proceeded by a single space. Mind that you need to account for both "year" and "years", depending on the result.
    
def calculate_age(year_of_birth, current_year):
    diff = year_of_birth - current_year
    if diff == -1:
        return "You are 1 year old."
    elif diff < -1:
        return "You are " + str(abs(diff)) + " years old."
    elif diff == 1:
        return "You will be born in 1 year."
    elif diff > 1:
        return "You will be born in " + str(diff) + " years."
    else:
        return "You were born this very year!"
    
    
# You get any card as an argument. Your task is to return a suit of this card.

def define_suit(card):
    if "S" in card:
        return "spades"
    elif "C" in card:
        return "clubs"
    elif "D" in card:
        return "diamonds"
    else:
        return "hearts"
    
    
# The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!

def say_hello(name):
    return "Hello, " + name


# Implement a function which convert the given boolean value into its string representation.

def boolean_to_string(b):
    if b == True:
        return "True"
    else:
        return "False"
    
    
# Define a function that removes duplicates from an array of numbers and returns it as a result.

def distinct(seq):
    return list(dict.fromkeys(seq))


# You can print your name on a billboard ad. Find out how much it will cost you. Each letter has a default price of £30, but that can be different if you are given 2 parameters instead of 1.
# You can not use multiplier "*" operator.
# If your name would be Jeong-Ho Aristotelis, ad would cost £600. 20 leters * 30 = 600 (Space counts as a letter).

def billboard(name, price=30):
    import numpy as np
    return np.multiply(len(name), price)

    
# Given an array of integers your solution should find the smallest integer.

def find_smallest_int(arr):
    return min(arr)


# Given an array of integers, return a new array with each value doubled.

def maps(a):
    b = [element * 2 for element in a]
    return b
    
