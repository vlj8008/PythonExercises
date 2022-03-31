#1. Create a class and using init method to assign these attributes to an object. 

class Property:

    def __init__(self, Property_number, Address, Num_rooms, Num_bathrooms):
    
        self.Property_number = Property_number #attributes
        self.Address = Address
        self.rooms = Num_rooms #notice how don't have to match.
        self.bathrooms = Num_bathrooms

    def prop_details(self): #method (not function)
        msg ='\nProperty Rooms: {}\nProperty Address: {}'.format(self.rooms,self.Address)
        return msg

#2. Create an object from the above class using init method

prop_1 = Property(1,"121 Main St", 3, 2) # instantiation of the object.

prop_2 = Property(2, "123 How St",2,2) #instantiating property 2 object
    

    
#Create a child of the Property class:

class Rental(Property): #now have inherited all the attributes and methods from parent (Property)
    
   def __init__(self,Property_number, Address, Num_rooms, Num_bathrooms,Rented):
    self.Number = Property_number
    self.Address = Address
    self.rooms = Num_rooms
    self.bathrooms = Num_bathrooms
    self.Rented = Rented

   def rental_info(self):
    print("Rented: {}".format(self.Rented)) 

#Create an object from the child class

prop_3 = Rental(3, "1 Happy Rd", 5, 5, "yes")
prop_4 = Rental(4, "2 Ocean Way" , 2, 1, "no")
   

if __name__== "__main__":

    print(prop_3.Rented)
    print(prop_2.Address)
    print(prop_3.prop_details())
    prop_3.rental_info()
    prop_4.rental_info()
    print(prop_4.prop_details())
    
    


   

    



    
    
