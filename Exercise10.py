def oddoreven(num):#created a function named "oddoreven" with the parameter "num"
    if num % 2:
    #calculates the users number, if number has a remainder then it will be odd
        print("Your number is odd")
    else:
    #or else if the users number has no remainder then it's even.
        print("Your number is even")
    
num = int(input("Put any number to check if its odd or even "))
#asks the user for a number which then get converted to an integer.

oddoreven(num)#calls the function