
#Creating a database in RAM using Python and SQLite

#Python 3.9.5

#Tested on OS Windows 10

#Written by Vicky Lee Jones

import sqlite3

connection = sqlite3.connect(':memory:')

c = connection.cursor()

c.execute("CREATE TABLE Roster (FirstName TEXT, Species TEXT, IQ INT)")
    
connection.commit()

c.execute("INSERT INTO Roster VALUES('Jean-Baptiste Zorg', 'Human', 122)")

connection.commit()

peopleValues = (('Korben Dallas', 'Meat Popsicle', '100'), ('Ak\'not', 'Mangalore', '-5'))

c.executemany("INSERT INTO Roster VALUES(?,?,?)",peopleValues)



c.execute("UPDATE Roster SET Species=? WHERE FirstName=?",('Human','Korben Dallas'))

connection.commit()

#c.execute("SELECT * FROM Roster")
#for row in c.fetchall():
    #print(row)


c.execute("SELECT FirstName, IQ  FROM Roster WHERE Species= 'Human'")
for row in c.fetchall():
    print(row)

connection.close()



