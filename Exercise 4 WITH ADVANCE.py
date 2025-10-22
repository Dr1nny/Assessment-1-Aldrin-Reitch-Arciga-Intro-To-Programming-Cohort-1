"""
Exersice 4: Primitive quiz
"""



print("Let's find out if you know all of the 10 capitals of European countries!")

points = 0

ans1 = (input("What is the capital of France? "))
fix1 = ans1.capitalize()

if fix1 == "Paris":
    print("You are Correct! Next Question!")
    points+=1
else:
    print("Your Answer is wrong!")

ans2 = (input("What is the capital of Italy? "))
fix2 = ans2.capitalize()

if fix2 == "Rome":
    print("You are Correct! Next Question!")
    points+=1
else:
    print("Your Answer is wrong!")

ans3 = (input("What is the capital of Spain? "))
fix3 = ans3.capitalize()

if fix3 == "Madrid":
    print("You are Correct! Next Question!")
    points+=1
else:
    print("Your Answer is wrong!") 
    