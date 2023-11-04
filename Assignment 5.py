import random
n=int(input("how long is the list="))
a=[]
for i in range(n):
    i=random.randint(1,60)
    a.append(i)
print(a)

