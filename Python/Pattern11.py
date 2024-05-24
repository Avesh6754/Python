i=6
j=9

for i in range(1,6):
    for k in range(1,(6-i)+1):
        print(end="  ")
    for j in range(1,9+1):
        if (j==1 or i==5 or i==2 and j>2 and j<4 or i==3 and j>4 and j<6 or i==4 and j>6 and j<8):
            print("*",end=" ")
        else:
            print(" ",end=" ")
      
    print()
