from random import randint

hayang = 0
kulob = 1

ako = (input("Humpyang makulong mahayang!: "))

c1 = randint(0, 1)
c2 = randint(0, 1)
c3 = randint(0, 1)  

print(f"Ako: {'kulob' if ako == kulob else 'hayang'}")
print(f"C1: {'kulob' if c1 == kulob else 'hayang'}")
print(f"C2: {'kulob' if c2 == kulob else 'hayang'}")
print(f"C3: {'kulob' if c3 == kulob else 'hayang'}")

if (ako == hayang and c1 == kulob and c2 == kulob and c3 == kulob):
    print("You win!")
elif (ako == kulob and c1 == hayang and c2 == hayang and c3 == hayang):
    print("You win!")
elif (ako == kulob and c1 == hayang and c2 == kulob and c3 == kulob):
    print("C1 wins!")
elif (ako == hayang and c1 == kulob and c2 == hayang and c3 == hayang):
    print("C1 wins!")
elif (ako == kulob and c1 == kulob and c2 == hayang and c3 == kulob):
    print("C2 wins!")
elif (ako == hayang and c1 == hayang and c2 == kulob and c3 == hayang):
    print("C2 wins")
elif (ako == kulob and c1 == kulob and c2 == kulob and c3 == hayang):
    print("C3 wins!")
elif (ako == hayang and c1 == hayang and c2 == hayang and c3 == kulob):
    print("C3 wins!!")
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
