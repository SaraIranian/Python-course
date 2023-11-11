def a():
    for row in game:
        for col in row:
            print(col, end="")
        print()
def game_winner ():
    if game[0][0]==" 0 " and game[0][1]==" 0 " and game[0][2]==" 0 ":
       print (player_1,"wins")
       quit()
    if game[0][0]==" 0 " and game[1][1]==" 0 " and game[2][2]==" 0 ":
       print (player_1,"wins")
       quit()
    if game[1][0]==" 0 " and game[1][1]==" 0 " and game[1][2]==" 0 ":
       print (player_1,"wins")
       quit()
    if game[2][0]==" 0 " and game[2][1]==" 0 " and game[2][2]==" 0 ":
       print (player_1,"wins")
       quit()
    if game[0][2]==" 0 " and game[1][1]==" 0 " and game[2][0]==" 0 ":
       print (player_1,"wins")
       quit()
    if game[0][0]==" 0 " and game[1][0]==" 0 " and game[2][0]==" 0 ":
       print (player_1,"wins")
       quit()
    if game[0][1]==" 0 " and game[1][1]==" 0 " and game[2][1]==" 0 ":
       print (player_1,"wins")
       quit()
    if game[0][2]==" 0 " and game[1][2]==" 0 " and game[2][2]==" 0 ":
        print (player_1,"wins")
        quit()
    if game[0][0]==" x " and game[0][1]==" x " and game[0][2]==" x ":
       print (player_2,"wins")
       quit()
    if game[0][0]==" x " and game[1][1]==" x " and game[2][2]==" x ":
       print (player_2,"wins")
       quit()
    if game[1][0]==" x " and game[1][1]==" x " and game[1][2]==" x ":
       print (player_2,"wins")
       quit()
    if game[2][0]==" x " and game[2][1]==" x " and game[2][2]==" x ":
       print(player_2,"wins")
       quit()
    if game[0][2]==" x " and game[1][1]==" x " and game[2][0]==" x ":
       print (player_2,",wins")
       quit()
    if game[0][0]==" x " and game[1][0]==" x " and game[2][0]==" x ":
       print (player_2,"wins")
       quit()
    if game[0][1]==" x " and game[1][1]==" x " and game[2][1]==" x ":
       print (player_2,"wins")
       quit()
    if game[0][2]==" x " and game[1][2]==" x " and game[2][2]==" x ":
        print(player_2,"wins")
        quit()
def game_over():
    if game[0][0]!=" - " and game[0][1]!=" - "and game[0][2] != "-"and game[1][0]==" - " and game[1][1]==" - " and game[1][2]==" - " and game[2][0]==" - " and game[2][1]==" - " and game[2][2]==" - ":
        print("no winner / game over")
        quit()
game=[[" - ", " - ", " - "],
      [" - ", " - ", " - "],
      [" - ", " - ", " - "]]
player_1=input("palyer1 enter your name=")
player_2=input("palyer2 enter your name=")
while True:
    while True:
        print(player_1)
        row=int(input("enter row="))
        col=int(input("enter col="))
        if row<3 and row>=0 and 3>col and col>=0:
            if game [row][col]==" - ":
                game[row][col]= " 0 "
                a()
                game_winner()
                break
            else:
                print("the cell is taken")
        else:
            print("enter a number between 0,1,2")
    if game_over():
        break
    
    while True:
        print(player_2)
        row=int(input("enter row="))
        col=int(input("enter col="))
        if row<3 and row>=0 and 3>col>=0:
            if game [row][col]==" - ":
                game[row][col]= " x "
                a()
                game_winner()
                break
            else:
                print("the cell is taken")
        else:
            print("enter number between 0,1,2")
    if game_over():
        break
