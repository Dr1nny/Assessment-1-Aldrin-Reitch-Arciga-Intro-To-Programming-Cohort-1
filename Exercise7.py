#some counting


print("===")#create a gap to reduce confusion
print("Increments of 1")#will print a text on the console to display what increments/decrements are shown

for a in range(51):
    #range(51 (how many iterations it will do, once it reaches desired, it will stop.))
    print(a)#will print till it reaches the desired. output = 0 -> 50

print("===")#create a gap to reduce confusion
print("Decrements of 1")#will print a text on the console to display what increments/decrements are shown

for b in range(50, -1, -1):
    #range(50 (start = 50), -1 (end = -1 ), -1(steps = -1))
    print(b)#prints the variable till it reaches its final output = 50 -> 0

print("===")#create a gap to reduce confusion
print("Increments of 1")#will print a text on the console to display what increments/decrements are shown

for c in range(30, 51, 1):
    #range(30 (start = 30), 51 (end = 51 ), 1(steps = 1))
    print(c) #output will be increments going from 30 -> 50
    
print("===")#create a gap to reduce confusion
print("Decrements of 2")#will print a text on the console to display what increments/decrements are shown

for d in range(50, 9, -2):
    #range(50 (start = 50), 9 (end = 9 ), -2(steps = -2))
    print(d)#output = 50, 45...,10
    
print("===")#create a gap to reduce confusion
print("Increments of 5")#will print a text on the console to display what increments/decrements are shown

for e in range(100, 201, 5):
    #range(100 (start = 100), 201 (end = 201 ), 5(steps = 5))
    print(e)#output = 100, 105,...,200