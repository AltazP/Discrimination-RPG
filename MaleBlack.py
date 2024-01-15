#Import getkey so that the user can the board correctly
from getkey import getkey, keys
#import os so I can clear the screen later
import os
#Import functions from different files in the program
from Board import board
from Continue import cont
from Smile import *
from food import hunger
#Define function that prints situation for black male in school. Parameters will be name, mental state and food level. Having the parameters will let me use these values in the situation
def bmschool(a, b, c):
  #Prints hunger and mental state
  hunger(c)
  print (end = "   ")
  smile(b)
  #Explains situation to user
  print ("\nYou are at school!")
  print ("You are a little late and are walking to class when the hall monitor stops you. He says \"Come here. Why are you skipping class\".\n\nHow do you respond")
  #while true for error catching
  while True:
    #gets user input
    q1 = input("1. \"I'm just walking to class right now\"\n2. Run and don't look back\n")
    #clears screen
    os.system('clear')
    #if user picks first option, a specific situation is printed 
    if q1 == "1":
      print ("Hall Monitor: \"Are you really?\" \nYou: \"Yes really\" \nHall Monitor: \"Ok hurry up and get to class\"")
      print ("\n You wonder why the hall monitor stopped you and not the other kids, but think nothing of it.\nMental Score remains the same")
      cont()
      #second situation is given
      print ("You hear some kids calling you racial slurs. How do you react?")
      #while true allows for error catching
      while True:
        #gets user input
        q2 = input("1. Ignore them and walk away. \n2. Insult them. \n3. Go up and punch the person\n")
        #clears screen
        os.system('clear')
        #if user picks first option, they are given a specific situation
        if q2 == "1":
          print ("You feel a little bad, but are used to hearing these words.\nMental score goes down 1")
          #mental score is decreased by 1
          b -= 1
          #prints mental score
          smile (b)
          cont()
          #breaks loop
          break
        #if second option is picked another situation is ran
        elif q2 == "2":
          #tells user the situation
          print ("You start calling the person a bunch of names, and make fun of his weight. This causes him to cry, and you feel pretty happy.\nMental score goes up 3")
          #mental score goes up 3
          b += 3
          #mental score is outputted
          smile (b)
          cont()
          #loop is broken
          break
        #if user chooses third option, another situation is given
        elif q2 == "3":
          #situation is explained
          print ("You punch the bully in the face. ")
          print ("This leads to your suspension, and the bully getting the final laugh\nMental score goes down 5")
          #mental score goes down 5
          b -= 5
          #mental score is outputted
          smile (b)
          cont()
          #loop is broken
          break
        #if user doesn't input a valid answer, they are asked to reinput a number
        else:
          print ("Invalid input. Please enter 1, 2, or 3.")
      #food is decreased by 3
      c -= 3
      #food and mental state is shown
      hunger(c)
      print (end = "   ")
      smile(b)
      #User is then taken out of the school situation
      print ("Your school day is over and you have now lost 3 food levels. Where do you decide to go next?")
      cont()
      break
    #if user chose the second option to the very first question, they are given another sitation
    elif q1 == "2":
      #situation is explained
      print ("You run and get to class. You got away.")
      cont()
      print ("Or at least that is what you though until the Principal came knocking on your class door\n")
      print ("Principal:\"" + a, "come down to the office with me right now\"")
      cont()
      print ("You regret running from the hall monitor. This causes your mental score to go down 1")
      #mental state goes down 1 and is displayed
      b -= 1
      smile(b)
      cont()
      print ("The Principal decides a 3 day suspension is valid as your punishment because the hall monitor claims that you tripped him, even though you did not.\nYou are very upset.\n\nMental score goes down 5")
      #mental state goes down 5 and is displayed
      b -= 5
      smile(b)
      cont()
      #hunger goes down 3, and mental state and hunger are displayed
      c -= 3
      hunger(c)
      print (end = "   ")
      smile(b)
      #tells user that their school day is over and user is take out of school situatioin
      print ("Your schol day is over and you have lost 3 food levels. Where do you decide to go next?")
      cont()
      break
    #if user didn't input a valid response to the first question they are asked to reinput an answer
    else:
      print ("Invalid input. Please enter 1 or 2")
  #mental state is returned
  return b


#!!!!!!!
#ALL THE FOLLOWING SITUATIONS FOLLOW THE SAME FORMAT AS THE PREVIOUS FUNCTION> THEREFORE COMMENTS WILL NOT BE ADDED!!!!
#!!!!!!!
def bmwork(a, b, c):
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
      print ("\nThey tell you that they expected you to be unsafe because of your skin colour, but then they let you know that they are very sorry for their actions")
      cont()
      print ("They say you have helped them realize they were wrong.\n This causes your mental score to go up 5")
      b += 5
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
      print ("Coworker1: \"What did you tell the boss.\"\nYou: \"Just how I felt like I didn't belong.\"\nCoworker1: \"Well of course you don't. Look at your skin colour.\"")
      cont()
      print ("This deeply hurt your feelings. your mental score goes down 7")
      b -= 7
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
def bmshop(a, b, c):
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("\nYou are at the grocery store!")
  print ("As you're walking around you see an elderly caucasian lady tyring to grab something from the top shelf, in which she is clearly sruggling. You go to help her and she says \"Get away from me Blackie.\"\n This upsets you, so what do you do next.")
  while True:
    q = input("1. Walk away. \n2. Tell her \"My name isn't blackie old hag\"\n")
    os.system('clear')
    if q == "1":
      print ("You walk away and move on with your day. This stitutation makes you a little upset so your mental score decreases by 3.")
      b -= 3
      smile (b)
      cont()
      break
    elif q == "2":
      print ("You call the lady an old hag and this results in her telling the manager what you said.")
      print ("The manager comes over so you tell him what she said, but all the manager tells you is \"Watch yourself, this is your first and final warning\"")
      cont()
      print ("This makes you pretty upset. Mental score goes down 6.")
      b -= 6
      smile (b)
      cont()
      break
    else:
      print ("Invalid input. Please enter 1 or 2")
 
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("\nYou need some things for your house so you are just looking around. You can't seem to find the frozen fruits so you go up to a worker to ask where they might be. He says \"I don't know.\" and then mutters a racial slur under his breath")
  cont()
  while True:
    q1 = input("Do you decide to\n1. Confront him \n2. Tell his manager\n")
    os.system('clear')
    if q1 == "1":
      print ("The worker gets mad and says \"You heard what I said\"")
      while True:
        q2 = input("Do you decide to \n1. Hit him \n2. Argue with him \n3. Just walk away\n")
        os.system('clear')
        if q2 == "1":
          print ("You hit the worker, and this leads to the situation escalating and the police being called.")
          print ("You get put in handcuffs but you end up getting off without consequences")
          cont()
          print ("Your whole day is ruined. Mental score goes down 10")
          b -= 10
          smile (b)
          break
        elif q2 == "2":
          print ("You argue with the worker which leads to his manager showing up. After explaining the situation the worker looses his job.")
          cont()
          print ("You feel like the worker got what he deserved but at the same time feel like the arguement was a waste of time. Mental score does not change.")
          smile (b)
          break
        elif q2 == "3":
          print ("You walk away.\nThen you hear the worker calling you and he says \"Sorry for my words, I was just having a really bad day.\" He then apologizes countless more times, which makes you feel better.")
          cont()
          print ("Mental Score goes up 5")
          b += 5
          smile (b)
          break
        else:
          print ("Invalid input. Please enter 1, 2, or 3.")
      cont()
      break
    elif q1 == "2":
      print ("You tell the workers manager about his actions. The manager has a talk with the worker.")
      cont()
      print ("Then he comes back even more mad, and calls you multiple more racial slurs before leaving.")
      print ("This causes your mental score to go down 5")
      b -= 5
      smile (b)
      cont()
      break
    else:
      print ("Invalid input. Please enter 1 or 2")
  c -= 3
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("looking at all this food made you hungry. Food level goes down 3, and you leave the store.")
  cont()
  return b
def bmrest(a, b, c):
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("You go to eat a place your friend recomended to you.")
  print ("As you're eating a kid comes up to you and compliments your hat.\nThen you hear his mom tell him, \"stay away from this guy, he's dangerous.\"")
  cont()
  while True:
    q1 = input("Do you decide to\n1. Just ignore her \n2. Insult her \n3. Say something nice about her\n")
    os.system('clear')
    if q1 == "1":
      print ("You ignore her and the mom and child walk away. But your feelings are still hurt.")
      cont()
      print ("Mental score goes down 3, but at least you got food. Food also goes up 5.")
      b -= 3
      c += 5
      smile (b)
      hunger (c)
      cont()
      break
    elif q1 == "2":
      print ("You insult the mother, but she tells the restaurant manager what you said.\n You get kicked out of the restaurant and are now upset. But at least you got some food")
      cont()
      print ("Mental score goes down 7 and food goes up 5")
      b -= 7
      c += 5
      smile (b)
      hunger (c)
      cont()
      break
    elif q1 == "3":
      print ("You compliment the mother, and this causes her to feel bad for what she said to you, and then apologizes. Her son later comes back and tells you how you are an awesome guy.")
      cont()
      print ("This makes you happy. Mental score goes up 7")
      b += 7
      c += 5
      smile (b)
      hunger (c)
      cont()
      break
      
    else:
      print ("Invalid input. Please enter 1 or 2.")
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("\nyou leave the restaurant. Where do you decide to go next?")
  cont()
  return b

