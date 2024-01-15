#Import getkey so that the user can the board correctly
from getkey import getkey, keys
#import os so I can clear the screen later
import os
#Define the board function. Parameter will let me know where to place the user on the board
def board(a): 
  os.system('clear')
  a = a.lower().strip()
  # x and y sets the users location
  #if a = home user starts outside of home on the board
  if a == "home":
    x = 4
    y = 4
  #if a = school user starts outside of school on the board
  elif a == "school":
    x = 1
    y = 1
  #if a = rest user starts outside of the restaurant on the board
  elif a == "rest":
    x = 2
    y = 7
  #if a = work user starts outside of work on the board
  elif a == "work":
    x = 8
    y = 8
  #if a = shop user starts outside of the grocery store on the board
  elif a == "shop":
    x = 8
    y = 3
    
  #Set the coordinates of school
  schoolx = 0
  schooly = 1
  #Set the coordinates of work
  workx = 8
  worky = 9
  #Set the coordinates of shop
  shopx= 9 
  shopy = 3
  #Set the coordinates of restaurant
  restx = 1
  resty = 7

  #Set symbols for each location
  school = "[S]"
  pos = "[+]"
  work = "[W]"
  shop = "[G]"
  rest = "[R]"

  #Sets what the board will look like (10x10 board)
  board = [["[ ]" for a in range (10)]for b in range (10)]

  #prints out the symbol at the specific locations of each place
  board[x][y]= pos
  board[schoolx][schooly] = school
  board[workx][worky] = work
  board[shopx][shopy] = shop
  board[restx][resty] = rest

  #While true will let the user keep inputting a direction
  while True:
    #tells the user what each symbol means
    print ("LEGNEND:\n[S] = School \n[R] = Restaurant \n[G] = Grocery Store \n[W] = Work\n") 
    #prints out the board
    for i in board:
      print (" ".join(i))
    #Gets user input for direction they want to move in
    print ("\nUse WASD or the arrow keys to move\npress \"e\" to go back home")
    key = getkey()

    #Clear the screen
    os.system('clear')

    #Checks if user wants to go up
    if key == keys.UP or key == keys.W:
      #clears users current location
      board[x][y] = "[ ]"
      #x-=1 makes the user go up 1
      x -= 1
      #stops the user from going off the board
      if x < 0:
        x = 0
      #sets new location to the position symbol
      board[x][y] = "[+]"
    
    #NEXT LINES OF CODE DO THE SAME THING AS LINES 76-85, JUST DIFFERENT DIRECTIONS
    elif key == keys.DOWN or key == keys.S:
      board[x][y] = "[ ]"
      x += 1
      if x > 9:
        x = 9
      board[x][y] = "[+]"
    elif key == keys.LEFT or key == keys.A:
      board[x][y] = "[ ]"
      y -= 1
      if y < 0:
        y = 0
      board[x][y] = "[+]"
    elif key == keys.RIGHT or key == keys.D:
      board[x][y] = "[ ]"
      y += 1
      if y > 9:
        y = 9
      board[x][y] = "[+]"
    elif key == keys.E:
      break

    #If user reachs any location the loop breaks, and they are then unable to move
    if board[x][y] == board[schoolx][schooly]:
      break
    elif board[x][y] == board[workx][worky]:
      break
    elif board[x][y] == board[shopx][shopy]:
      break
    elif board[x][y] == board[restx][resty]:
      break
  #Depending on which location the user is at, a number between 1 and 5 is outputted.
  if board[x][y] == board[schoolx][schooly]:
    return 1
  elif board[x][y] == board[workx][worky]:
    return 2
  elif board[x][y] == board[shopx][shopy]:
    return 3
  elif board[x][y] == board[restx][resty]:
    return 4
  else:
    return 5
