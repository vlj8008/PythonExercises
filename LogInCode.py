
class User:
    name = "no name provided" #need to give default values. Can not leave blank
    email = ""
    password = "123abc"
    account = 0

    def login(self): #this is called "method" not "function" as it is specific to the "user" class
        entry_email = input("Enter your email: ")
        entry_pw = input("Enter your password: ")
        if (entry_email == self.email and entry_pw == self.password):
            print("Welcome back {}".format(self.name))
        else:
            print("You are not authorized for this page")

new_user = User()

new_user.login()
