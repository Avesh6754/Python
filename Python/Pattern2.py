i=6
j=6

for i in range(1,6):
    for j in range(1,6):
        if (j==1 and j>0 and j<2 or i==1 or j==5 or i==5):
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()