num=int(input("How many times you need to use the calculator:"))
for i in range(num):
    import math
    op= input("enter op(+, /, *, -, sin, cos, tan, cot, factorial, sqrt):")
    if op=="sin":
        x=int(input("enter x:"))
        r=(math.sin(math.radians(x)))
    if op=="cos":
        x=int(input("enter x:"))
        r=(math.cos(math.radians(x)))
    if op=="tan":
        x=int(input("enter x:"))
        r=(math.tan(math.radians(x)))
    if op=="cot":
        x=int(input("enter x:"))
        z=(math.tan(math.radians(x)))
        r=1/z
    if op=="factorial":
        x=int(input("enter x:"))
        r=(math.factorial(x))
    if op=="sqrt":
        x=int(input("enter x:"))
        r=(math.sqrt(x))
    if op=="+":
        a=float(input("enter a:")) 
        b=float(input("enter b:"))
        r=a+b
    if op == "/":
        a=float(input("enter a:")) 
        b=float(input("enter b:"))
        if b==0:
                r="Error"
        else:
                r=a/b
    if op == "*":
        a=float(input("enter a:")) 
        b=float(input("enter b:"))
        r=a*b
    if op == "-":
        a=float(input("enter a:")) 
        b=float(input("enter b:"))
        r=a-b
    print(r)