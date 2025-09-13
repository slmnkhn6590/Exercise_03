rows = 4
cols = 8

for row in range(rows):
    for col in range(cols):
        if (row + col) % 2 == 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()