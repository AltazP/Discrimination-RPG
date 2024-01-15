#Import getkey so that the user can the board correctly
from getkey import getkey, keys
#import os so I can clear the screen later
import os
#import functions from different files in the program
from Board import board
from Continue import cont
from Smile import *
from food import hunger
#!!!!!
#ALL THE FUNCTIONS IN THIS FILE ARE IN THE SAME FORMAT AS THE FIRST FUNCTION IN THE MALEBLACK FILE SO COMMENTS HAVE NOT BEEN ADDED.
#TO SEE HOW IT IS FORMATTED GO TO FIRST FUNCTION IN MALEBLACK FILE!!!
#!!!!!
def bfschool(a, b, c):
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("\nYou are at school!")
  print ("You are a little late and are walking to class when the hall monitor stops you. He says \"Come here. Why are you skipping class\".\n\nHow do you respond")
  while True:
    q1 = input("1. \"I'm just walking to class right now\"\n2. Run and don't look back\n")
    os.system('clear')
        
    if q1 == "1":
      print ("Hall Monitor: \"Are you really?\" \nYou: \"Yes really\" \nHall Monitor: \"Ok hurry up and get to class\"")
      print ("\n You wonder why the hall monitor stopped you and not the other kids, but think nothing of it.\nMental Score remains the same")
      cont()
      print ("You hear some kids calling you racial slurs. How do you react?")
      while True:
        q2 = input("1. Ignore them and walk away. \n2. Insult them. \n3. Go up and punch the person\n")
        os.system('clear')
        if q2 == "1":
          print ("You feel a little bad, but are used to hearing these words.\nMental score goes down 1")
          b -= 1
          smile (b)
          cont()
          break
        elif q2 == "2":
          print ("You start calling the person a bunch of names, and make fun of his weight. This causes him to cry, and you feel pretty happy.\nMental score goes up 3")
          b += 3
          smile (b)
          cont()
          break
        elif q2 == "3":
          print ("You punch the bully in the face. ")
          print ("This leads to your suspension, and the bully getting the final laugh\nMental score goes down 5")
          b -= 5
          smile (b)
          cont()
          break
        else:
          print ("Invalid Input. Please enter 1, 2, or 3")
      c -= 3
      hunger(c)
      print (end = "   ")
      smile(b)
      print ("Your school day is over and you have now lost 2 food levels. Where do you decide to go next?")
      cont()
      break
    elif q1 == "2":
      print ("You run and get to class. You got away.")
      cont()
      print ("Or at least that is what you though until the Principal came knocking on your class door\n")
      print ("Principal:\"" + a, "come down to the office with me right now\"")
      cont()
      print ("You regret running from the hall monitor. This causes your mental score to go down 1")
      b -= 1
      smile(b)
      cont()
      print ("The Principal decides a 3 day suspension is valid as your punishment because the hall monitor claims that you tripped him, even though you did not.\nYou are very upset.\n\nMental score goes down 5")
      b -= 5
      smile(b)
      cont()
      c -= 3
      hunger(c)
      print (end = "   ")
      smile(b)
      print ("\nYour schol day is over and you have lost 3 food levels. Where do you decide to go next?")
      cont()
      break
    else:
      print ("Invalid input. Please enter 1 or 2")
  return b
def bfwork (a, b, c):
  hunger(c)
  print (end = "   ")
  smile (b)
  print ("\nYou are at work!")
  print ("You have been working at your current job for a good bit of time, and feel like you deserve a raise.")
  cont()
  while True:
    q1 = input("Do you decide to \n1. Ask your boss for a raise. \n2. Just keep working and hope you get one eventually\n")
    os.system('clear')
    if q1 == "1":
      print ("Boss: \"Hi", a + ", can I help you?\"")
      print ("You: \"Yes I was thinking about how I have worked here for a long time, and was wondering if I could get a raise\"")
      print ("Boss: \"Okay let me think about it\"")
      cont()
      print ("You leave the bosses office and then hear him talking to another one of your coworkers who is a male.")
      cont()
      print ("Boss: \"Hey Josh, I've seen you working hard and am giving you a raise\"")
      print ("Josh: \"Thank you so much sir, but what about", a +".\"")
      print ("Boss: \"" + a , "is a female and isn't getting anywhere in her career. It's funny how she even thought she could get a promotion\"")
      print ("Josh: \"Hahaha you're right boss.\"")
      cont()
      print ("This hurts your feelings.")
      while True:
        q2 = input("Do you decide to \n1. Confront the boss \n2. Keep working\n")
        if q2 == "1":
          print ("Boss: \"Can I help you", a +"?\"")
          print ("You: \"Yes I heard you talking to Josh, and what you said was totally unfair.\"")
          print ("Boss:\"Well too bad, who said life's fair?\"")
          cont()
          while True:
            q3 = input("What do you do?\n1. say \"Ok well I quit.\"\n2. Go back to work\n")
            os.system('clear')
            if q3 == "1":
              print ("You quit and are now left without a job, but you realize your current job was going to get you no where.")
              print ("You realize there are only better opportunities ahead, Mental score goes up 5")
              b += 5
              smile (b)
              cont()
              break
            elif q3 == "2":
              print ("You go back to your desk and continue working. This encounter made you very upset though, so your mental score goes down 7")
              b -= 7
              smile (b)
              cont()
              break
            else:
              print ("Invalid input. Please enter 1 or 2.")
          break
        elif q2 == "2":
          print ("You go back to working at your desk, but listening to what your boss said makes you upset. Mental score goes down 5.")
          b -= 5
          smile (b)
          cont()
          break
        else:
          print ("Invalid input. Please enter 1 or 2.")
      break
    elif q1 == "2":
      print ("You continue working and hope a raise will eventually come. Mental score does not change")
      cont()
      break
    else:
      print ("Invalid input. Please enter 1 or 2")
      smile (b)
      cont()
      break
  c-=3
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("\nYou finish working and your food level goes down 3. Where do you go next?")
  cont()
  return b
def bfshop (a, b, c):
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("\nYou are at the grocery store!")
  print ("You are walking around when you hear someone make an inappropriate comment about you.")
  cont()
  while True:
    q1 = input("Do you decide to \n1. Slap the man \n2. Ignore the man \n3. Tell an employee\n")
    os.system('clear')
    if q1 == "1":
      print ("You slap the man but this results in his calling you a racial slur and calling an employee over.")
      print ("You tell the employee what happened but he tells you that because you hit the man you have to leave the grocery store")
      cont()
      print ("You leave the store but everything that happened results in you feeling very upset. Mental score goes down 8.")
      b -= 8
      smile (b)
      cont()
      break
    elif q1 == "2":
      print ("You ignore the man and continue shopping, but the comment the man made still upsets you. Mental score goes down 3.")
      b -= 3
      cont()
      break
    elif q1 == "3":
      print ("You see an employee and tell him what the man told you. The employee then escorts the man out of the store, but before leaving he apologizes to you.")
      cont()
      print("This makes you feel better and therefore your mental score goes up 5.")
      b += 5
      smile (b)
      cont()
      break
    else:
      print ("Invalid input, please enter 1 or 2.")
  c-=3
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("\nYou finish shopping and looking at all this food makes your food level go down 3. Where do you go next?")
  cont()
  return b
def bfrest (a, b, c):
  hunger(c)
  print (end = "   ")
  smile(b)
  print ("You go to eat a place your friend recomended to you.")
  print ("As you're eating a little girl comes up to you and compliments your makeup.\nThen you hear her mom tell her, \"Those people are disgusting and criminals.\"")
  print ("Hearing this makes up upset, so what do you do next?")
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
      print ("You insult the mother, but she tells the restaurant manager what you said.\n The kid also hears what you called her mom, and is visibly upset.")
      print ("You get kicked out of the restaurant and but you are upset. At least you got some food")
      print ("Mental score goes down 7 and food goes up 5")
      cont()
      break
    elif q1 == "3":
      print ("You compliment the mother, and this causes her to feel bad for what she said to you, and then apologizes. Her daughter later comes back and tells you how you are an awesome person.")
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