import random #imports module called "Random"

print(random.randrange(1,100)) #prints a random number between 1 and 100


age1 = 20
age2 = 21

key = True


if age1 == age2:
    
    
    
        print("You are both the same age")

    

elif  age1 < age2:
    print("you are younger than your partner")

else:

    

    print("you are older than your partner")

    

age = 0

check = print(bool(age))

if check == False:

    print("Please enter your name")


def myFunction():
    return False

if myFunction() == True:
    print('Yes')

else:
    print('no')



x = "twenty"
print(isinstance(x,str))

#FOR LOOP

i = 0 #initialised the variable "i" and set it to 0

for i in range(1,10,1): #range function returns sequence of numbers from 0 - 9 
    print("{} iteration through the loop.".format(i)) # curly bracket is placeholder. Format method puts formatted string in to
    #curly braces which is the place holder. 
    i += 1 #every cycle add one to the i variable
    

#WHILE LOOP

i = 0
while i < 10:
    print("{} iteration through the loop. ".format(i))
    i += 1

# WHILE LOOP #2 WITH BREAK STATEMENT
i = 0

while i<=20:
    print('gone through loop {} time.'.format(i))
    if i == 14:
        break
        
    i = i + 1

# while loop # 2 with continue statement

i = 0

while i < 20:
    

    i += 1
    
    if i == 4:
        continue #continue keyword means "stop current iteration and continue with the next.

    print('gone through iteration {} times'.format(i))
    

else: print("we have come to the end of the loop ! Yay!")

#for loop using "range"

i = 0

for i in range(11):

    print( 'this is the {} time through the loop'.format(i))

    i = i+1


# for loop not using range,


pets = ["dog", "cat", "bird"]

for x in pets:
    

    if x == "cat":
        continue #this means exit the loop

    print("pet " + x)

#use range function

    i = 0

    for i in range(1,12,2):
        print(i)

        i = i + 1

    else: print("we have come to the end now")

#loop an array challenge

    name = 'Python'

    print(len(name))

    for i in enumerate(name):
        print(i)
        

    
     



