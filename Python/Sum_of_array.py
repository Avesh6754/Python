import numpy as np
data =[]

element=int(input("Enter how many element to enter : "))
for i in range (element):
    data.append(int(input("Enter the element : {i}")))
print(sum(data))
