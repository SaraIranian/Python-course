import random
the_number=random.randint(0,30)
count=0
while True: 
    count+=1
    your_number=int(input("Enter a number"))
    if the_number==your_number:
        print("you got it!!")
        break
    if your_number<the_number:
        print("enter a higher number")
    if your_number>the_number:
        print("enter a lower number")
print ("the number is",the_number, "you have guessed",count ,"times")