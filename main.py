'''
Altaz P.
RPG that puts the user in the shoes of different races and genders
'''
#Import getkey so that the user can the board correctly
from getkey import getkey, keys
#import os so I can clear the screen later
import os
#Next lines of code import files from the program so that they can run in this main file
from Board import board
from Continue import cont
from Smile import smile
from MaleBlack import *
from FemaleBlack import *
from MaleAsian import *
from FemaleAsian import *
from food import hunger
#Set the users identity to an array
identity = ["name", "gender", "race"]
#Set the current mental score to 10
mental_score = 10
#Set food level to 5
food = 5
#Set count to 0 for running the program a specific number of times later
count = 0
#gets user identity and sets it to identity array
def ident ():
  #Global identity lets me user identity in this function
  global identity
  #setting identity to default so the program runs if this is the users second time running it
  identity = ["name", "gender", "race"]
  #Tells the user what the program does
  print ("This is a role playing game where you will be in the shoes of a specific race and/or sexual orientation.")
  #Gets name input
  name = input("First, what is your name? ")
  #Changes identity array. Adds inputted name to array
  identity.remove("name")
  identity.insert(0, name)
  #While true is for error checking
  while True:
    #Asks user to input a gender
    gender = input("What is your gender?\n1. Male\n2. Female\n")
    #If user inputs 1 their gender is male
    if gender == "1":
      gender = "Male"
      break
    #if user enters 2 their gender is female
    elif gender == "2":
      gender = "Female"
      break
    #if user inputs neither 1 nor 2 they get asked to reinput a number
    else:
      print ("Invalid Input. Please enter 1 or 2.")
    #changes "Gender" in the identity array to their gender
  identity.remove("gender")
  identity.insert(1, gender)

  #While True is used for error checking
  while True:
    #Asks user their race
    race = input("What is your race?\n1. Black \n2 East Asian\n")
    #Sets race to the race they inputted
    if race == "1":
      race = "Black"
      break
    elif race == "2":
      race = "East Asian"
      break
    #If user doesn't input 1 or 2 they are asked to reinput  a number
    else:
      print ("Invalid Input. Please enter 1 or 2.")
    #Changes "race" in the identity array with the race the user picked
  identity.remove("race")
  identity.insert(2, race)
#Function to print out intro message
def intro():
  #global food to use food in the function
  global food
  
  #prints what the goal of the game is
  print ("Hi", identity[0] + ", you are going to be playing this game as if you were a", identity[2], identity[1] + ".\nThe goal of this game is to keep your mental score as high as possible, whilst also taking care of yourself.")
  #cont clears the screen and asks the user to press enter to continue
  cont()
  #tells user what their mental score can be seen as, as well as their hunger level
  print ("Your mental score can be defined as the following images.\n😁 = Amazing \n😊 = Good \n😐 = Alright \n😢 = Bad\nAs well as a number.")
  print ("\nYour hunger can be seen as the following image 🍖. Your hunger ranges from 1 - 10 so try to stay as full as you can")
  
  cont()
  #prints out users hunger level
  hunger(food)
  #end lets the users mental score be on the same line as their hunger level
  print (end = "   ")
  #prints mentals score
  smile(mental_score)
  #Intro message
  print ("\n\nIt's a bright and sunny Monday morning and you are so happy that the week is finally coming to an end. You eat get ready for your day and to leave your house.\nFood level goes up 3.\n\nPress enter to leave your house.")
  #increases food level by 3
  food += 3
  cont()
#main function that runs everything
def main():
  #Global count food and mental score so I can use them in this function
  global count
  global food
  global mental_score
  #While true will let the program loop if the user wants to rerun it
  while True:
    #prints out identity and intro functions
    ident()
    intro()
    #Checks if the user is a black male
    if identity[1] == "Male" and identity[2] == "Black":
      #prints out the board that lets the user pick where they want to go
      #The function will output where the user goes
      found = board("home")
      #next line of code runs the program until the user has gone to 4 places, or if their mental score is too low
      while count < 4 and mental_score >= -10:
        #if the user has no food the program stops and they are given a message that lets them know they have finished the game
        if food <= 0:
          print ("You are out of food, and therefore pass out. You go back home and go to bed.")
          break
        #if found = 1 the user is at school
        if found == 1:
          #blop will be set to mental score and the program will print out the situation I have made for black male at school
          blop = bmschool(identity[0], mental_score, food)
          #mental score is set to blop value, because blop is updated mental score
          mental_score = blop
          #Because the user has gone through one situation, count is increased by 1 and their food goes down 3
          count += 1
          food -= 3
          #board is printed out again, but the user location is outside of school
          found = board("school")
        #if found = 2 the user is at work
        elif found == 2:
          #blop will be set to mental score and the program will print out the situation I have made for black male at work.
          blop = bmwork(identity[0], mental_score, food)
          #mental score is set to blop value, because blop is updated mental score
          mental_score = blop
          #Because the user has gone through one situation, count is increased by 1 and their food goes down 3
          count += 1
          food -= 3
          #board is printed out again, but the user location is outside of work.
          found = board("work")
        #if found = 3 the user is at the grocery store
        elif found == 3:
          #blop will be set to mental score and the program will print out the situation I have made for black male at the grocery store.
          blop = bmshop(identity[0], mental_score, food)
          #mental score is set to blop value, because blop is updated mental score
          mental_score = blop
          #Because the user has gone through one situation, count is increased by 1 and their food goes down 3
          count += 1
          food -=3
          #board is printed out again, but the user location is outside of the store.
          found = board("shop")
        #if found = 4 the user is at the restaurant
        elif found == 4:
          #blop will be set to mental score and the program will print out the situation I have made for black male at the restaurant.
          blop = bmrest(identity[0], mental_score, food)
          #mental score is set to blop value, because blop is updated mental score
          mental_score = blop
          #Because the user has gone through one situation, count is increased by 1. Because user went to the resaurant their food level goes up 5
          count += 1
          food += 5
          #board is printed out again, but the user location is outside of the store.
          found = board("rest")
          #if found = 5 user decided to go home
        elif found == 5:
          #while True will allow me to do some error catching
          while True:
            #Asks the user if they want to go back out
            print ("You are back home. Do you want to go back out?")
            q = input("1. Yes \n2. No\n")
            #if user enters a valid input the loop stops
            if q == "1" or q == "2":
              break
            #If user inputs something other than 1 or 2 they are asked to reinput a number
            else:
              print ("Invalid input. Please enter 1 or 2")
          #if user wanted to end the program they are taken out of the game
          if q == "2":
            break
          #if user wants to continue playing they start back outside their house
          elif q == "1":
            found = board("home")
            
  #!!!!!!
  #LINES 186 - 314 HAVE THE SAME LAYOUT AS LINES 112-184. SO NO COMMENTS HAVE BEEN ADDED
  #!!!!!!
    elif identity[1] == "Female" and identity[2] == "Black":
      found = board("home")
      while count < 4 and mental_score >= -10:
        if food <= 0:
          print ("You are out of food, and therefore pass out. You go back home and go to bed.")
          break

        if found == 1:
          blop = bfschool(identity[0], mental_score, food)
          mental_score = blop
          count += 1
          food -= 3
          found = board("school")
        elif found == 2:
          blop = bfwork(identity[0], mental_score, food)
          mental_score = blop
          count += 1
          food -= 3
          found = board("work")
        elif found == 3:
          blop = bfshop(identity[0], mental_score, food)
          mental_score = blop
          count += 1
          food -=3
          found = board("shop")
        elif found == 4:
          blop = bfrest(identity[0], mental_score, food)
          mental_score = blop
          count += 1
          food += 5
          found = board("rest")
        elif found == 5:
          while True:
            print ("You are back home. Do you want to go back out?")
            q = input("1. Yes \n2. No\n")
            if q == "1" or q == "2":
              break
            else:
              print ("Invalid input. Please enter 1 or 2")
          if q == "2":
            break
          elif q == "1":
            found = board("home")
            
    elif identity[1] == "Male" and identity[2] == "East Asian":
      found = board("home")
      while count < 4 and mental_score >= -10:
        if food <= 0:
          print ("You are out of food, and therefore pass out. You go back home and go to bed.")
          break

        if found == 1:
          blop = amschool(identity[0], mental_score, food)
          mental_score = blop
          count += 1
          food -= 3
          found = board("school")
        elif found == 2:
          blop = amwork(identity[0], mental_score, food)
          mental_score = blop
          count += 1
          food -= 3
          found = board("work")
        elif found == 3:
          blop = amshop(identity[0], mental_score, food)
          mental_score = blop
          count += 1
          food -=3
          found = board("shop")
        elif found == 4:
          blop = amrest(identity[0], mental_score, food)
          mental_score = blop
          count += 1
          food += 5
          found = board("rest")
        elif found == 5:
          while True:
            print ("You are back home. Do you want to go back out?")
            q = input("1. Yes \n2. No\n")
            if q == "1" or q == "2":
              break
            else:
              print ("Invalid input. Please enter 1 or 2")
          if q == "2":
            break
          elif q == "1":
            found = board("home")
    elif identity[1] == "Female" and identity[2] == "East Asian":
      found = board("home")
      while count < 4 and mental_score >= -10:
        if food <= 0:
          print ("You are out of food, and therefore pass out. You go back home and go to bed.")
          break

        if found == 1:
          blop = afschool(identity[0], mental_score, food)
          mental_score = blop
          count += 1
          food -= 3
          found = board("school")
        elif found == 2:
          blop = afwork(identity[0], mental_score, food)
          mental_score = blop
          count += 1
          food -= 3
          found = board("work")
        elif found == 3:
          blop = afshop(identity[0], mental_score, food)
          mental_score = blop
          count += 1
          food -=3
          found = board("shop")
        elif found == 4:
          blop = afrest(identity[0], mental_score, food)
          mental_score = blop
          count += 1
          food += 5
          found = board("rest")
        elif found == 5:
          while True:
            print ("You are back home. Do you want to go back out?")
            q = input("1. Yes \n2. No\n")
            if q == "1" or q == "2":
              break
            else:
              print ("Invalid input. Please enter 1 or 2")
          if q == "2":
            break
          elif q == "1":
            found = board("home")
    #If the game ended because the users mental score was too low, they are displayed the following message
    if mental_score < -10:
      print ("Your mental score is now at the bottom. Your character is extremely depressed so they go home and contemplate their life.")
      cont()
    #If the game ended because the user went to 4 different places they are displayed ther following message
    if count == 4:
      print ("You realize how late it is and how tired you are, so you go home.")
    #Next lines print the ending message
    print ("Your day is now over. Thanks for playing my RPG game.")
    print ("This is your final mental state. Remember, Higher means better.")
    smile(mental_score)
    cont()
    #Asks the user if they would like to play again
    while True:
      repeat = input("Would you like to play again? (please enter yes or no)\n").lower()
      if repeat == "yes" or repeat == "no":
        break
      else:
        print ("Invalid input. Please enter 1 or 2.")
    if repeat == "no":
      break
  
main()