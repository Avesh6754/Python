file_name="Hello world "
file= open("demo3.txt","w")
file.write(file_name)
file.close()
try:
    
    file= open("demo2.txt","r")
    print(file.read())
   
except:
    print("File Not Found :")
