namelist=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#creating a list of names using the variable "namelist"

print(namelist)
#prints the lists from the namelist to display for the user
ui=input("Please Choose a name from the list: ")
#ask the user to choose a name from the list

if ui in namelist:#
#This code uses an if else statement where it checks if the user input is in the namelist
    print("You have succefully picked", ui,"from the list")
else:
    print("The name is not from the list")
#if the name isn't on namelist, then this will be displayed to the user