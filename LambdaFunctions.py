#normal function

#def mult(x):   #name of function is "mult"
    #return 3*x + 1

#print(mult(2))

#lambda x: 3*x + 1 #lambda is a keyword and not the name of the function. Lambda says what follows is an

                    #anomonys function. You can use it by giving it a name ie the letter "g"

pay = lambda hr : hr * 30
print(pay(10))

location1 = "Clearwater"
location2 = "Austin"

print(" I would rather live in {} than {}".format(location1, location2))


x = format(3, 'b')
print(x)

print("binary: {0:b}, hexadecimal: {0:x}, percentage: {0:%}".format(4))

def getSum(num1, num2):
    answer = num1 + num2
    print("The answer is {}.".format(answer))

getSum(2,4)

myAdd = getSum

myAdd(6,4)



import math
help(math)

truth1 = True
truth2 = False
print("the truth is always {}.".format(truth2))







    

