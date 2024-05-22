import numpy as np

data =[]
elem = int(input("Enter the size of array : "))

for i in range(elem):
    data.append(int(input("Enter the value of array : ")))
    data.sort()
print(data)

