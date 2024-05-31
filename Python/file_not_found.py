file_name=input("Enter the data : ")

try:
    file= open("demo3.txt","w")
    file.write(file_name)
    file.close()
    file= open("demo2.txt","r")
    print(file.read())
   
except:
    print("File Not Found :")
