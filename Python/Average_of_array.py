import numpy as np

def Avearge(element,data):
    for i in range (element):
        data.append(int(input("Enter the element : {i}")))
    print(int(sum(data)/element))
data =[]

element=int(input("Enter how many element to enter : "))
Avearge(element,data)