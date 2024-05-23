i=6
j=9

for i in range(1,6):
    for k in range(1,(6-i)+1):
        print(end=" ")
    for j in range(1,9):
        if (j==1 or i==5 or j==8):
            print("*",end=" ")
        else:
            print(" ",end=" ")
      
    print()