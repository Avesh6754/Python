import numpy as np

data =[]
elem = int(input("Enter the size of array : "))

for i in range(elem):
    data.append(int(input("Enter the value of array : ")))
print(data)

max=data[0]
for i in range(elem):
    if data[i]>max:
        max=data[i]

print(max)