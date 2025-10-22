"""
Exersice 4: Primitive quiz

"""

print("Let's find out if you know all of the 10 capitals of European countries!")
#prints to the console

points = 0
#added a point variable to store and summarize the total of correct answers

ans1 = (input("\nWhat is the capital of France? ")).capitalize()
"""
ans1 is a variable that will store the user input. The ".capitalize()" will help
correct the miss-capitalization of the user input

example:
    
with the help of .capitalize(),  "pArIs" can be converted to "Paris"

"""
#Will be using if-else statement to check if the user is right or wrong.

if ans1 == "Paris":
    #will check if ans1 variable is the same exact text that was given to look for.
    print("You are Correct! Next Question!")
    points+=1
    #if answer is correct, will print a text to the user that they are correct
    #will add a point for being correct and store to the points variable
else:
    print("Your Answer is wrong!")
    #if the answer is wrong, it will display a message to the user that they are incorrect.
    #will not receive a point.


ans2 = (input("\nWhat is the capital of Italy? ")).capitalize()
if ans2 == "Rome":
    #will check if ans2 variable is the same exact text that was given to look for
    print("You are Correct! Next Question!")
    points+=1
    #if answer is correct, will print a text to the user that they are correct
    #will add a point for being correct and store to the points variable
else:
    print("Your Answer is wrong!")
    #if the answer is wrong, it will display a message to the user that they are incorrect.
    #will not receive a point.
    

ans3 = (input("\nWhat is the capital of Spain? ")).capitalize()
if ans3 == "Madrid":
    #will check if ans3 variable is the same exact text that was given to look for
    print("You are Correct! Next Question!")
    points+=1
    #if answer is correct, will print a text to the user that they are correct
    #will add a point for being correct and store to the points variable
else:
    print("Your Answer is wrong!") 
    #if the answer is wrong, it will display a message to the user that they are incorrect.
    #will not receive a point.
    
    
ans4 = (input("\nWhat is the capital of United Kingdom ")).capitalize()
if ans4 == "London":
    #will check if ans4 variable is the same exact text that was given to look for
    print("You are Correct! Next Question!")
    points+=1
    #if answer is correct, will print a text to the user that they are correct
    #will add a point for being correct and store to the points variable
else:
    print("Your Answer is wrong!")
    #if the answer is wrong, it will display a message to the user that they are incorrect.
    #will not receive a point.
    

ans5 = (input("\nWhat is the capital of Netherlands? ")).capitalize()
if ans5 == "Amsterdam":
    #will check if ans5 variable is the same exact text that was given to look for
    print("You are Correct! Next Question!")
    points+=1
    #if answer is correct, will print a text to the user that they are correct
    #will add a point for being correct and store to the points variable
else:
    print("Your Answer is wrong!")
    #if the answer is wrong, it will display a message to the user that they are incorrect.
    #will not receive a point.
    

ans6 = (input("\nWhat is the capital of Greece? ")).capitalize()
if ans6 == "Athens":
    #will check if ans6 variable is the same exact text that was given to look for
    print("You are Correct! Next Question!")
    points+=1
    #if answer is correct, will print a text to the user that they are correct
    #will add a point for being correct and store to the points variable
else:
    print("Your Answer is wrong!")
    #if the answer is wrong, it will display a message to the user that they are incorrect.
    #will not receive a point.
    

ans7 = (input("\nWhat is the capital of Denmark? ")).capitalize()
if ans7 == "Copenhagen":
    #will check if ans7 variable is the same exact text that was given to look for
    print("You are Correct! Next Question!")
    points+=1
    #if answer is correct, will print a text to the user that they are correct
    #will add a point for being correct and store to the points variable
else:
    print("Your Answer is wrong!") 
    #if the answer is wrong, it will display a message to the user that they are incorrect.
    #will not receive a point.
    
    
ans8 = (input("\nWhat is the capital of Ireland? ")).capitalize()
if ans8 == "Dublin":
    #will check if ans8 variable is the same exact text that was given to look for
    print("You are Correct! Next Question!")
    points+=1
    #if answer is correct, will print a text to the user that they are correct
    #will add a point for being correct and store to the points variable
else:
    print("Your Answer is wrong!")
    #if the answer is wrong, it will display a message to the user that they are incorrect.
    #will not receive a point.

ans9 = (input("\nWhat is the capital of Russia? ")).capitalize()
if ans9 == "Moscow":
    #will check if ans9 variable is the same exact text that was given to look for
    print("You are Correct! Next Question!")
    points+=1
    #if answer is correct, will print a text to the user that they are correct
    #will add a point for being correct and store to the points variable
else:
    print("Your Answer is wrong!") 
    #if the answer is wrong, it will display a message to the user that they are incorrect.
    #will not receive a point.
    
    
ans10 = (input("\nWhat is the capital of Germany? ")).capitalize()
if ans10 == "Berlin":
    #will check if ans10 variable is the same exact text that was given to look for
    print("You are Correct! Next Question!")
    points+=1
    #if answer is correct, will print a text to the user that they are correct
    #will add a point for being correct and store to the points variable
else:
    print("Your Answer is wrong!") 
    #if the answer is wrong, it will display a message to the user that they are incorrect.
    #will not receive a point.
    
    
if points ==10:#using an if-else statement for checking of points
    print("\nCongratulations! You have a score of:",points,"/10")
    #if user gets 10/10, it will congratulate the user.
else:
    print("\nGood Job! You have:",points,"/10, you can try again for a higher score!")
    #if the user does not reach the full score, will display to the user that they can try again
    