i=65
j=70

for i in range(65,70):
    for j in range(65,70):
        if (j==65 and j>64 and j<66 or i==65 or j==69 or i==69):
            print(chr(j),end=" ")
        else:
            print(" ",end=" ")
    print()