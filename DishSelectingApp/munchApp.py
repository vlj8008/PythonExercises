'''
Munch App MVP
v0.1.0
By Vicky Jones

App produces a dinner menu from favourite dishes, and produces a shopping list of
ingredients if required.

A. Functions
A1 Choose meals function
A2 Build shopping list function

B. Lists

1. ask user how many days
2. generate a random menu list (making sure there is no double up on menu list)
3. ask if user wants a shopping list
4. generate a shopping list or exit app
'''
from random import choice #just importing choice method, not whole "random" module.

name = 'Vicky'
FavMeals = ['pizza', 'burgers', 'fish and chips', 'tacos', 'pie', 'omlette', 'soup'] #made variable FavMeals in to list
Menu = [] #created empty global variable called "Menu" as an empty list.

def chooseDish(days): #pass in days variable which we got from below input code.
    
    while len(Menu)< days :
        chosenDish = choice(FavMeals) #chosenDish is local variable. "Choice" is built in function that selects random item in list
        if chosenDish not in Menu:
            Menu.append(chosenDish) #add the chosen dish to "Menu"
    for i in Menu:
         #this for loop prints each item of the menu one under another to make look better.
        
        print('Item {}: {}'.format(Menu.index(i)+1,i))
        

PizzaIng = ['cheese', 'flour base', 'tomato sauce']
BurgerIng = ['burger', 'cheese', 'bun']
FishChipsIng = ['fish', 'chips', 'batter']
TacosIng = ['taco', 'cheese', 'tomato']
PieIng = ['pastry', 'ground beef', 'gravy']
OmletteIng = ['egg', 'onion', 'cheese']
SoupIng = ['broth', 'carrots', 'onion']
ShoppingList = []
        

def shoppingList():
    if 'pizza'in Menu :
        ShoppingList.append(PizzaIng)
    if 'burgers' in Menu:
        ShoppingList.append(BurgerIng)
    if 'fish and chips' in Menu:
        ShoppingList.append(FishChipsIng)
    if 'tacos' in Menu:
        ShoppingList.append(TacosIng)
    if 'pie' in Menu:
        ShoppingList.append(PieIng)
    if 'omlette' in Menu:
        ShoppingList.append(OmletteIng)
    if 'soup' in Menu:
        ShoppingList.append(SoupIng)
    print() #prints an empty line to make look better. 
    for dish in ShoppingList:
        for ingredient in dish: #nested loop so we can print ingredients on separate line. 
            print(ingredient)
    print()
    print('Viola, bon appetit')

def endProgram(name):
    print()
    print('You got it {}, bye for now!'.format(name))
        
if __name__ == "__main__":
        

    print('Hello, my name is Munch. I am going to generate a meals list for you')
    answer = input("How many days would you like me to plan?")
    days = int(answer) #change input result to integer as it is always string in Python
    print('Great, I will make a meal plan for {} day(s)'.format(answer))
    
    chooseDish(days) #calling chooseDish function.
    
    #data normalization measures:
    while True: #setting up a loop
        answer =input('Would you like a printout of the shopping list? Answer "y" or "n"')
        if answer in('y','n', 'Y', 'N'): #using "in" keyword to see if the answer variable is in the tuple
            break #if it is, break from the while loop.
        else:
            print("please enter correctly")
            
    if answer in('y', 'Y'):
        shoppingList() #calling function if answer is yes.
        

    else:
        endProgram(name)
    


 






    
    
    
