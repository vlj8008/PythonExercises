

#class should make use of a private attribute or function.

#class should make use of a protected attribute or function.

class Protected:

    

    def __init__(self):
        self.__privateVar = 10 #private variable (attribute) indicated by double underscore. 

    
                                    


    def _mult_by_variable(self): #protected method indicated by single underscore.
        a = 10 # does not change the behaviour of method
        result = a * self.__privateVar #. Acts as warning to other developers and states "this is protected, don't use outside of class
    

        
        print(result)

    




if __name__ == "__main__":

    obj = Protected() #instantiating the object class
    obj._mult_by_variable() #calling the protected _mult_by_variable method and making use of the private attribute.
    
