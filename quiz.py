G = 0
R = 0
H = 0
S = 0

a = int(input("Q1) Do you like Dawn or Dusk?\n    1) Dawn\n    2) Dusk\n"))

if a == 1:
    G += 1
    R += 1
elif a == 2:
    H += 1
    S += 1
else:
    print("Wrong input")


b = int(input("Q2) When I’m dead, I want people to remember me as:\n    1) The Good\n    2) The Great\n    3) The Wise\n    4) The Bold\n"))

if b == 1:
    H += 1
elif b == 2:
    S += 1
elif b == 3:
    R += 1
elif b == 4:
    G += 1
else:
    print("Wrong input")



c = int(input("Q3) Which kind of instrument most pleases your ear?\n    1) The violin\n    2) The trumpet\n    3) The piano\n    4) The drum\n"))

if c == 1:
    S += 1
elif c == 2:
    H += 1
elif c == 3:
    R += 1
elif c == 4:
    G += 1
else:
    print("Wrong input")

if H == 3 or H == 2:
    print("Hufflepuff")
elif S == 3 or S == 2:
    print("Slytherin")
elif G == 3 or G == 2:
    print("Gryffindor")
elif R == 3 or R == 2:
    print("Ravenclaw")
else:
    print("inconclusive \n try again") # you get this result when the answers are 1 1 1 or 1 2 2 or 2 3 4 or 2 4 3
