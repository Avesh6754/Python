import numpy as np

data=[]
newdata=[]
row=int(input("Enter the row : "))
colum=int(input("Enter the colum : "))

for i in range(row):
    for j in range(colum):
        data.append(int(input("Enter the value of array : ")))

print(data,end=" ")

newrow=int(input("Enter the row : "))
newcolum=int(input("Enter the colum : "))

for i in range(newrow):
    for j in range(newcolum):
        newdata.append(int(input("Enter the value of array : ")))

print(newdata,end=" ")

print(data+newdata)