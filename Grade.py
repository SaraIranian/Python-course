Name=input("Enter your first name:")
Familyname=input("Enter your family name:")
Math=int(input("Enter your Math Score:"))
English=int(input("Enter your English Score:"))
Physics=int(input("Enter your Physics Score:"))
Average=(Math+English+Physics)/3
print(Name, Familyname, ("Your Average equals="),Average)
if Average>=17:
    print("Your status is Great")
    if 12<=Average<12:
        print("Your status is Normal")
        if Average<12:
            print("Your status is fail")