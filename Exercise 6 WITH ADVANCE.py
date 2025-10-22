
password="12345"#variable to store password
guesses=5#number of attempts
while guesses > 0:#is guesses more than 0? If yes, then it will loop, if false loop will stop.
    login=(input("Enter your password: "))
    #creating login variable to store user input
    if login == password:
        print("Logged in, welcome user!")
        break#using break to stop looping
    else:
        guesses -= 1#minus the guesses variable
        print("Incorrect Password, Remaining Attempts:", guesses)
        
if guesses == 0:
    #once variable guesses reaches 0, it will display the following below.
    print("\nAttempt Limit Reached, Contacting Authorities...")