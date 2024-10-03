k = 1
z = []
for y in range(9):
    z.append("|___|")


for j in range(1, 10):
    if j % 2 == 0:
        u1 = int(input("Where do you want to go? ")) - 1
        if z[u1] == "|___|":
            z[u1] = "|_O_|"
        else:
            print("You lost your chance")
            k -= 1
    else:
        u2 = int(input("Where do you want to go? ")) - 1
        if z[u2] == "|___|":
            z[u2] = "|_X_|"
        else:
            print("You lost your chance")
            k -= 1

    print("After turn ", k)
    print(z[0], z[1], z[2])
    print(z[3], z[4], z[5])
    print(z[6], z[7], z[8])
    print("              ")


    w = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    if any(all(z[i] == "|_O_|" for i in c) for c in w):
        print("O wins!")
        break
    elif any(all(z[i] == "|_X_|" for i in c) for c in w):
        print("X wins!")
        break
    elif j ==9:
        print("DRAW")
    k += 1