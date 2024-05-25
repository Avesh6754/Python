i=69
j=73
for i in range(65,69+1):
    for k in range(i,(65+5)):
        print(" ",end=" ")
    for j in range(65,73+1):
        if (j==65 or i==69 or i==66 and j>66 and j<68 or i==67 and j>68 and j<70 or i==68 and j>70 and j<72):
        
            print( chr(j),end=" ")
        else:
            print(" ",end=" ")  
    
    print()