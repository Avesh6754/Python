
def Bubble(a,list):
    temp=0
    for i in range (0,len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp

    return list


list =[]
a=int(input("Enter the size of array : "))
for i in range (a):
    list.append(int(input("Enter the value of array : ")))
print(Bubble(a,list))


