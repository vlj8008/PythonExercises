
#The parent class should have at least one method (function).

class User:

    def __init__(self,Name,Email,password):
        self.name = Name
        self.email = Email
        self.password = password

    def logIn(self): # Parent class method
        entry_name = input("Enter your name:")
        entry_email = input("Enter your email:")
        entry_password = input("Enter your password:")

        if(entry_email == self.email and entry_password == self.password):
                print("Welcome back, {}".format(entry_name))
        else:
                print("The password or email is incorrect")

user_1 = User("Bob","bob@gmail.com","abc123")
user_2 = User("Sally", "sally@gmail.com", "password")

#Child class - Subscriber

class Subscriber(User): #this code pulls in all the attributes and methods from parent.
    def __init__(self, Name, Email, basic_plan, premium_plan, pin):  
        self.email = Email
        self.basic_plan = basic_plan
        self.premium_plan = premium_plan
        self.pin_number = pin

    def logIn(self):
        entry_name = input("Enter your name:")
        entry_email = input("Enter your email:")
        entry_pin = input("Enter your pin:")
        """this is polymorphism, meaning taking a method from
        the parent and changing it. """ 

        if(entry_email == self.email and entry_pin == self.pin_number):
                print("Welcome back, {}, you have {} subscribed to the premium plan".format(entry_name, self.premium_plan))
        else:
                print("The pin or email is incorrect")

subscriber_1 = Subscriber("Jane", "jane@gmail.com", "yes", "not", "12ab")

#Child class - Executive (with additional security questions)

class Executive(User):
    def __init__ (self, Name, Email, password, pin, security, security_clearance):
        self.name = Name
        self.email = Email
        self.password = password
        self.pin_number = pin
        self.security_password = security
        self.security_clearance = security_clearance
        

    def logIn(self):
        entry_name = input("Enter your name:")
        entry_email = input("Enter your email:")
        entry_password = input("Enter your password:")
        entry_pin = input("Enter your pin:")
        entry_security_pw = input("Enter your security password")
        
        if(entry_email == self.email and entry_pin == self.pin_number and entry_security_pw == self.security_password):
                print("Welcome back, {}, of security {}".format(entry_name, self.security_clearance))
        else:
                print("The pin or email is incorrect")

executive_1 = Executive("Jessica", "jessica@yahoo.com", "password", "123", "alpha","Level 3")
        


if __name__ == "__main__":

    print(executive_1.name)
    print(user_1.name)
    executive_1.logIn()

    
    
    

                


    
    
                









