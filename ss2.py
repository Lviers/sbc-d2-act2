from random import randint
#from flask import Flask , render_template

p1 = input("Humpyang makulong mahayang!: ")

c1 = randint(1,2)
c2 = randint(1,2)
c3 = randint(1,2)


if p1 == 1 and c1 == 2 and c2 == 2 and c3 == 2:
    print("You won!!")
elif p1 == 2 and c1 ==1  and c2 == 2 and c3 == 2:
    print("C1 won!")
elif p1 == 2 and c1 == 2 and c2 == 1 and c3 == 2:
    print("C2 Wins!")
elif p1 == 2 and c1 == 2 and c2 == 2 and c3 == 1:
    print("C3 Wins!")
if p1 == 2 and c1 == 1 and c2 == 1 and c3 == 1:
    print("You won!!")
elif p1 == 1 and c1 ==2  and c2 == 1 and c3 == 1:
    print("C1 Wins!")
elif p1 == 1 and c1 ==1  and c2 == 2 and c3 == 1:
    print("C2 Wins!")
elif p1 == 1 and c1 == 1 and c2 == 1 and c3 == 2:
    print("C3 Wins!")
else:
    print("Draw!")





""""""

"""
light = False
plugged = True
burn = True

if light == True:
    if light == burn:
        print("WAHHHHHh")
    else:
        print("yippie")
else:
    print("putcha")    

age = 16

if age < 18:
    print("PEDO!")
else:
    print("~~")
    
"""