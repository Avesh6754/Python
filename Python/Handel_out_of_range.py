list =[]
x=int(input("Enter the value of x : "))

for i in range(x):
    list.append(int(input("Enter the value of array : ")))

n=int(input("Enter the index number for find number : "))
try:
    print(list[n])
except:
    print("index out of range ")
