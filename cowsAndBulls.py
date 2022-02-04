import random
print("Welcome to Cows and Bulls game!\n\n")
diff = int(input("Choose game difficulty 1-9: "))
def check():
    userCode = input("\nInsert {} digit code: ".format(diff))
    if userCode.isnumeric():
        if len(userCode) != diff:
            print("Wrong amonut of digits!")
            check()
        else:
            cows = bulls = q  = 0
            while q < len(userCode):
                if int(userCode[q]) == randomCode[q]: cows+=1
                elif int(userCode[q]) in randomCode: bulls+=1
                q+=1
            if cows == 1: print("You have {} cow".format(cows))
            else: print("You have {} cows".format(cows))
            if bulls == 1: print("You have {} bull".format(bulls))
            else: print("You have {} bulls".format(bulls))
            if cows == diff: print("\nYou win!")
            else:
                check()
    else: 
        print("Insert digits only!")
        check()
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