#Import getkey so that the user can the board correctly
from getkey import getkey, keys
#import os so I can clear the screen later
import os
#import functions from different files of the program
from Board import board
from Continue import cont
from Smile import *
from food import hunger
#!!!!!
#ALL THE FUNCTIONS IN THIS FILE ARE IN THE SAME FORMAT AS THE FIRST FUNCTION IN THE MALEBLACK FILE SO COMMENTS HAVE NOT BEEN ADDED.
#TO SEE HOW IT IS FORMATTED GO TO FIRST FUNCTION IN MALEBLACK FILE!!!
#!!!!!
def amschool(a, b, c):
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("\nYou are at school and in math class. As you are doing your work another student calls you a racial slur then tells you to do his math work.")
  print ("This makes you upset so what do you do?")
  cont()
  while True:
    q1 = input("1. Ignore the bully \n2. Tell the teacher\n")
    if q1 == "1":
      print ("You ignore the bully, but this makes him pick on you more.")
      print ("The bully then makes you do his math work, and you do it. This makes you upset.")
      cont()
      print ("Your mental score goes down 7")
      b-=7
      smile (b)
      cont()
      break
    elif q1 == "2":
      print ("You tell the teacher and they send the kid to the principal's office")
      print ("\nThe prinicipal then calls you down to the office as well and you explain how you were getting treated, so the bully gets suspended for 3 days.")
      cont()
      print ("This makes you feel a bit better. Mental score goes up 3")
      b+=3
      smile (b)
      cont()
      break
    else:
      print ("Invalid input. Please enter 1 or 2")
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("Your schol day is over and you have lost 3 food levels. Where do you decide to go next?")
  cont()
  return b
def amwork(a, b, c):
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("\nYou are at Work!")
  print ("You work an office job, with mostly caucasian people. You don't really feel included, so you decide to do something about it.")
  cont()
  while True:
    q1 = input("Do you\n1. Invite some coworkers to an event \n2. Tell your boss\n")
    os.system('clear')
    if q1 == "1":
      print ("Your coworkers agree to come, and everyone gets along well")
      print ("\nThey tell you that they expected you to be nasty because covid came from as well as other stereotypes, but then they let you know that they are very sorry for their actions.")
      cont()
      print ("They say you have helped them realize they were wrong.\n This causes your mental score to go up 7")
      b += 7
      smile (b)
      cont()
      c -= 3
      hunger(c)
      print (end = "   ")
      smile(b)
      print("\nYou finish working and your food level drops by 3. Where do you go next?")
      cont()
      break
    elif q1 == "2":
      print ("You tell your boss about your feelings. He lets you know that this situation is out of his hands")
      cont()
      print ("Your coworkers manage to find out about you telling the boss, so they confront you")
      print ("Coworker1: \"What did you tell the boss.\"\nYou: \"Just how I felt like I didn't belong.\"\nCoworker1: \"Well of course you don't. Look at what you look like.\"")
      cont()
      print ("This deeply hurt your feelings. your mental score goes down 8")
      b -= 8
      smile (b)
      cont()
      c -= 3
      hunger(c)
      print (end = "   ")
      smile(b)
      print("\nYou finish working and your food level drops by 3. Where do you go next?")
      cont()
      break
    else:
      print ("Invalid Input. Please enter 1 or 2")
  return b
def amshop(a, b, c):
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("\nYou are at the grocery store.")
  print ("You pass by someone with a limp and they acidentally bump into you.")
  print ("They then say, \"Can't see where you're going Jackie Chan?\"\nHow do you react to this racist remark")
  cont()
  while True:
    q1 = input("1. Just walk away \n2. Make fun of the persons limp")
    os.system('clear')
    if q1 == "1":
      print ("You ignore the comment and just go on with your shopping.")
      print ("As you're shopping the man comes back and apologizes for his comment and says his day hasn't been the best and he took it out on you.")
      cont()
      print("This makes you feel better, and therefore your mental score goes up 3")
      b += 3
      smile (b)
      cont()
      c -= 3
      hunger(c)
      print (end = "   ")
      smile(b)
      print("\nYou finish shopping but looking at all this food makes your food level drop by 3. Where do you go next?")
      cont()
      break
    elif q1 == "2":
      print ("You insult the mans limp, and you thought the comment was funny")
      print ("But then the man said he was a war veteren, which makes the comment you made very offensive")
      cont()
      print ("People around you heard you make fun of the man and tell a store employee, and they escort you out of the store")
      cont()
      print ("This makes you very upset. Mental score drops 7.")
      b-=7
      smile (b)
      cont()
      c -= 3
      hunger(c)
      print (end = "   ")
      smile(b)
      print("\nYou finish shopping but looking at all this food makes your food level drop by 3. Where do you go next?")
      cont()
      break
    else:
      print ("Invalid input, please enter 1 or 2")
  return b
  
def amrest(a, b, c):
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("\nYou are at a restaurant, and you take off your mask to eat.")
  print ("This is when you hear the group of people beside you make a comment about how people like you started COVID-19 and that you should just keep your mask on.")
  print ("How do you react?")
  cont()
  while True:
    q1 = input("1. Move to a different table.\n2. Insult them \n3. Tell a worker what they said\n")
    os.system('clear')
    if q1 == "1":
      print ("You move to a different table, and the people you are now sitting beside are friendly, which makes you feel better")
      print ("This positive evens out the negative interaction you had just experienced")
      cont()
      print ("mental score does not change")
      smile (b)
      cont()
      break
    elif q1 == "2":
      print ("You insult the group of people, then they make fun of you more.")
      print ("You then just continue eating but their comments and attitude makes you really upset")
      cont()
      print ("Mental score goes down 5")
      b-=5
      smile (b)
      cont()
      break
    elif q1 == "3":
      print ("You tell a worker about what the group beside you said.")
      print ("The worker gives the group a warning about their actions")
      cont()
      print ("Then as you are eating the group apologizes to you for what they said, which makes you feel better")
      print ("Mental score goes up 5.")
      b+=5
      smile(b)
      cont()
      break
    else:
      print ("Invalid input, please enter 1, 2 or 3.")
  c-=3
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("\nYou finish eating and leave. Where do you go next?")
  cont()
  return b