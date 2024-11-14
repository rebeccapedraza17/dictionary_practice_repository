# Rebecca Pedraza
# Nov 14
# Dictionary practice

alien = {"home planet":"Mars",
         "skin color" :"green",
         "age":90, "number of eyes":90,
         "fingers" :"10 in each hand",
         "languages spoken":["spanish", "kligon", "dutch"]}
print(alien["age"])

for key in alien.keys():
    print(alien[key])

for key in alien.keys():
    print(key, alien[key])

for item in alien.items():
    print(item)

for key, value in alien.items():
    print(key, value)

    
'''
alien.keys()
alien.values()
alien.items()
'''
