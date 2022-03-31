
#parent class

class Organism:
    name = 'Unknown'
    species = 'Unknown'
    legs = None #this is special data type
    arms = None 
    dna = "Sequence A"
    origin = "unknown"
    carbon_based = True #data type Boolean. This will be inherited by all children even though this
    # is not explicitly stated in the children. 

    def information(self): #self keyword allows access to all info from class
        msg = "\nName: {}\nSpecies: {}\nLegs: {} \nArms: {} \nDNA: {} \nOrigin: {} \nCarbon Based: {}"\
        .format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

#child class instance

class Human(Organism): #the organism word within the parenthesis then allows inheritance.
    name = "Joe" # we overid the parent class values with our own ("Joe")
    species = "Homosapien"
    legs = 2
    arms = 2
    orgin = 'Earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg

#another child class instance

class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on it's target!"
        return msg

#another child class instance

class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = 'Mars'

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two seperate organisms !"
        return msg

if __name__== "__main__":

    human = Human() #instantiating human object
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())

    

    



