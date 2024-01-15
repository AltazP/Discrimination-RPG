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
def afschool(a, b, c):
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
def afwork (a, b, c):
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
def afshop (a, b, c):
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
def afrest(a, b, c):
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