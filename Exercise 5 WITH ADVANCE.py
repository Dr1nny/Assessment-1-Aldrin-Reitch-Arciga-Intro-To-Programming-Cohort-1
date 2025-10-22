#Days of the month Exersice 5

months={'1' : 31,
        '2' : 28,
        '3' : 31,
        '4' : 30,
        '5' : 31,
        '6' : 30,
        '7' : 31,
         '8' : 31,
        '9' : 30,
        '10' : 31,
        '11' : 30,
        '12' : 31}
#creating a dictionary to store the number of months with their respective days

number = (input("Please type a month number from 1-12 "))
#Will ask the user to put a number from 1-12, if an invalid number occurs, will end.

if number =='1':
    print(f"The month number {number} is January which has {months[number]} days")
    #output = "The month number 1 is january which has 31 days
elif number =='2':
    q = input("Is it currently a leap year? Answer in yes or no format. ").lower()
    #will ask if the current year is a leap year, using .lower will ensure the answer will stay lowercase.
    if q == "yes":
        months["2"] = 29
        print(f"The month number {number} is February which has {months[number]} days")
        #output = The month number 2 is February which has 29 days
    else:
        print(f"The month number {number} is February which has {months[number]} days")
        #output = The month number 2 is February which has 28 days
        
elif number =='3':
    print(f"The month number {number} is March which has {months[number]} days")
    #output = The month number 3 is March which has 31 days
    
elif number =='4':
    print(f"The month number {number} is April which has {months[number]} days")
    #output = The month number 4 is April which has 30 days

elif number =='5':
    print(f"The month number {number} is May which has {months[number]} days")
    #output = The month number 5 is May which has 31 days
    
elif number =='6':
    print(f"The month number {number} is June which has {months[number]} days")
    #output = The month number 6 is June which has 30 days

elif number =='7':
    print(f"The month number {number} is July which has {months[number]} days")
    #output = The month number 7 is July which has 30 days

elif number =='8':
    print(f"The month number {number} is August which has {months[number]} days")    
    #output = The month number 8 is August which has 31 days

elif number =='9':
    print(f"The month number {number} is September which has {months[number]} days")
    #output = The month number 9 is September which has 30 days

elif number =='10':
    print(f"The month number {number} is October which has {months[number]} days")
    #output = The month number 10 is October which has 31 days

elif number =='11':
    print(f"The month number {number} is Novemeber which has {months[number]} days")
    #output = The month number 11 is November which has 30 days

elif number =='12':
    print(f"The month number {number} is December which has {months[number]} days")
    #output = The month number 12 is December which has 31 days

else:
    print("That is an invalid month number.")
    """
    by failing to comply with the numbers 1-12, it will display the output:
    "That is an invalid month number"
    """