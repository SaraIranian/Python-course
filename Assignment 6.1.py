while True:
    op=input("start or exit=")
    if op=="exit":
        break
    list=[]
    n=int(input("enter n ="))
    m=int(input("enter m ="))
    for i in range(1,n+1):
        for z in range(1,m+1):
            print(i*z, end="")
            print()
