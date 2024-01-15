#Create a function that prints out a face depending on the mental score
def smile (a):
  #depending on a a different face is printed
  if a >= 20:
    print ("Mental State:", str(a) + "/😁")
  elif a >= 10 and a < 20:
    print ("Mental State:", str(a) + "/😊")
  elif a >=0 and a <10:
    print ("Mental State:", str(a) + "/😐")
  elif a < 0:
    print ("Mental State:", str(a) + "/😢")