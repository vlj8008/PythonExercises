
# important note: everything in Python is object

mySentence = ' loves the color'

color_list = ['red', 'blue', 'black', 'green', 'yellow'] # square bracket means list

def color_function(name): #parameter equals "name"
    lst = []  #list variable
    for i in color_list: #the i is a temporary variable which denotes the index number
        msg = "{0} {1} {2}".format(name,mySentence,i) #msg is variable
        lst.append(msg) #appends an element to the end of the list.
    return lst #returns back the variable to the program and leaves the loop

lst = (color_function('Vicky')) #calling function and passing argument "Vicky"
for i in lst:
    print(i)

#LOOP VIDEO

mySentence = ' loves the color'

color_list = ['red', 'blue', 'black', 'green', 'yellow'] # square bracket means list

def color_function(name): #parameter equals "name"
    lst = []  #list variable
    for i in color_list: #the i is a temporary variable which denotes the index number
        msg = "{0} {1} {2}".format(name,mySentence,i) #msg is variable
        lst.append(msg) #appends an element to the end of the list.
    return lst #returns back variable to the program and leaves the loop

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '': #if name is empty
            print('You need to provide your name please')
        elif name == 'Sally':
            print('Sally, you may not use this software') 
        else:
            go = False
            
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()

#CREATE A FUNCTION AND CALL A FUNCTION

property_data1 = '1 bedroom 1 bathroom apartment'

def details_output():
    print("The property you are looking at is " + property_data1)

details_output()

#ARRAY CHALLENGE


features = ['1 bedroom', '1 bathroom', 'apartment']

for y in features:
    print(y)

features.append('no garage')

for y in features:
    print(y)

print(features.count('1 bedroom'))

features.sort()

print(features)

features.append('bathroom')
features.sort()
print(features)

#PROGRAM SCOPE

name = "Python" #global variable

def getName():
    name = "c sharp" # this is accessed when function is called. This is a local variable. "Name" returns back to "python" after this function is called. 
    print("I am coding with {}".format(name))
getName()

fname = input("What is your 'first name?'\n>>>")

lname = input("What is your 'last name?'\n>>>")

print('Hello {} {}, how are you today ?'.format(fname,lname))

def Name():
    fname = input("Please type in your first name without any capitalizations.\n>>>").lower()
    print ("thankyou {}, welcome back ! ".format(fname))

Name()



    
    

          




    


