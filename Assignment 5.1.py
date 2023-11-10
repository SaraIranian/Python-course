n=int(input("enter the number of rows="))
m=int(input("enter the number of column="))
for i in range(n):
    for z in range(m):
        if (i+z)%2==0:
            print("#", end="")
        else:
            print("*",end="")
    print()