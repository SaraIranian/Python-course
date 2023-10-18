a=int(input("Enter a number for a"))
b=int(input("Enter a number for b"))
c=int(input("enter a number for c"))

if a+c>b:
    if a+b>c:
        if b+c>a:
            print("There is a triangle with these numbers")
else:
    print("You can not draw a triangle with these numbers")