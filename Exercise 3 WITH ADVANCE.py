"""
Exercise 3: Biography
"""


                            #Will ask a question depending which value is needed
biography = {'Name' : input("Please Put Your First Name: "),#key = name : value = input(will store what the user types in)
             'Second Name' : input("Please Enter Your Second Name: "),#key = second name : value = input (will store what the user types in)
             'Hometown' : input("Please Tell Your Hometown: "),#key = Hometown : value = input (will store what the user types in)
             'Age' : str(input("Please Tell Your Age: "))}#key = age : value = input (will store what the user types in)
                    #by adding a 'str' before the input it ensures that if asked for the age, even in letters like: twelve or ten, will accept and display on the age value.

print("\nFirst Name:",biography['Name'],"\nSecond Name:",biography['Second Name'],"\nHometown:",biography['Hometown'],"\nAge:",biography['Age'])
"""
Output:
    
First Name:(user input)
Second Name:(user input)
Hometown:(user input)
Age:(user input)
    

"""