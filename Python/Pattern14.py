i=5
j=5
n=1
for i in range(1,5+1):
    for k in range(i,6-1):
        print(end=" ")
    n=1
    for j in range(1,i+1):
        print(n,sep=" ",end=" ")
        n=n*(i-j)/j
    print()
