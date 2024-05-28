mystring=input("enter the string : ")
print(mystring)
count=0
newstring =input("Enter the character to find in string : ")

for i in mystring:
    if i==newstring:
        count+=1
print(count)