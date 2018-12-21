cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys: ")
for key in cast:
    print(key)

print("\nIterating through keys and value: ")
for key,value in cast.items():
    print("Actor: {}      Role: {}".format(key,value))

'''
Iterating through keys:
Jerry Seinfeld
Julia Louis-Dreyfus
Jason Alexander
Michael Richards

Iterating through keys and value:
Actor: Jerry Seinfeld      Role: Jerry Seinfeld
Actor: Julia Louis-Dreyfus      Role: Elaine Benes
Actor: Jason Alexander      Role: George Costanza
Actor: Michael Richards      Role: Cosmo Kramer
'''