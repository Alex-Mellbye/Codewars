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
        
    
        
    
    
    
    
    
    
    
    
    
