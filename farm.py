animal_legs={"chickens":2,"cows":4,"pigs":4}
def animals(no_chickens,no_cows,no_pigs):
   no_legs =no_chickens*animal_legs["chickens"]+no_cows*animal_legs["cows"]+no_pigs*animal_legs["pigs"]
   return (no_legs)

print(animals(2,3,5))
print(animals(1,2,3))
print(animals(5,2,8))

