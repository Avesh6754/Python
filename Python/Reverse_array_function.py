
import numpy 

def Reverse(list,elemen):

    list.reverse()
    print(list)

list = []
elemen=int(input("Enter the size of array : "))

for i in range (elemen):
    list.append(int(input("Enter the value of array : ")))
Reverse(list,elemen)
