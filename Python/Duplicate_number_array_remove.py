import numpy 
data =[]
x=int(input("Enter the size of array : "))
for i in range (x):
    data.append(int(input("enter the value of array : ")))


print(data)
newdata=[]
for i in data:
    if i not in newdata:
        newdata.append(i)

print(newdata)
