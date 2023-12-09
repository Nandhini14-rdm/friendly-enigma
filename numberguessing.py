import random
comp=random.randint(1,100)
user=int(input("Enter num: "))
i=0
while(i!=0):
    if(comp==user):
        print("congrats")
    elif(comp>user):
        print("Too high")
    elif(comp<user):
        print('Too low')
    
    i+=1
print(i)