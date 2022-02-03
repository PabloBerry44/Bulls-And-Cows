import random
print("Welcome to Cows and Bulls game!\n\n")
diff = int(input("Choose game difficulty 1-9: "))

def check():
#check if there are similarities and print gained points
    userInput = input("\nInsert {} digit code: ".format(diff))
    if len(userInput) != diff:
        print("Wrong amonut of digits!")
        check()
    else:
        userCode=[]
        for x in userInput:
            x=int(x)
            userCode.append(x)
        cows = 0
        bulls =0
        q = 0
        while q < len(userCode):
            if userCode[q] == randomCode[q]: cows+=1
            elif userCode[q] in randomCode: bulls+=1
            q+=1
        if cows == 1: print("You have {} cow".format(cows))
        else: print("You have {} cows".format(cows))
        if bulls == 1: print("You have {} bull".format(bulls))
        else: print("You have {} bulls".format(bulls))
        if cows == len(userCode): print("\nYou win!")
        else:
            check()

#create random code and save it to an array
randomCode = []
def getRandom():
    y = random.randint(1, 9)
    if y in randomCode: getRandom()
    else: randomCode.append(y)
z=0
while z < diff:
    getRandom()
    z+=1
check()

input("\nPress enter to exit")