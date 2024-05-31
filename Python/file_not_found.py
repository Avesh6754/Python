file_name=input("Enter the data : ")

try:
    file= open(file_name,"r")
    file.read()
    print(file_name)
    file.close()
except:
    print("File Not Found :")
