import random
print("\n")
print("----------Welcome to Rock Scissor Paper Game!!!----------")
print("\n")
print("Play with computer or Person?")
print("press c for computer or p for person: ")
choice = input()
print("\n")
if (choice=='c' or choice=='C'):
  print("Enter Person name:")
  user0=input(str())  
  user=int(input("%s enter 0 for rock, 1 for scissor or 2 for paper:" %(user0))) 
  comp=random.randint(0,2)
  print("Computer's choice is:",comp)
  if(user==comp):
    print("Game Draw `_`")
  elif(user==0 and comp==1 or user==1 and comp==2 or user==2 and comp==0):
    print("Yahooo! %s wins ;)" %(user0))
  else:
    print("Computer wins :(")

if (choice=='p' or choice=='P'):
  print("Enter Person1 name:")
  user11=input(str())
  print("Enter person2 name:")
  user22=input(str())
  print("\n")
  user1=int(input("%s enter 0 for rock, 1 for scissor or 2 for paper:" %(user11)))
  user2=int(input("%s enter 0 for rock, 1 for scissor or 2 for paper:" %(user22)))
  
  if(user1==user2):
    print("Game Draw `_`")
  elif(user1==0 and user2==1 or user1==1 and user2==2 or user1==2 and user2==0):
    print("Yahooo! %s Wins ;)"%(user11))
  else:
    print("Yahooo! %s Wins ;)"%(user22))