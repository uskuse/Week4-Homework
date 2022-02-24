import time,random,datetime
x = int(input("Enter your first number guess:"))
y = int(input("Enter your final number guess:"))
number = random.randint(x,y)
guess_number = 0
print("let the timer begin:")
now = datetime.datetime.now()
while True :
    yourGues = int(input("What is your Guess:"))
    if yourGues>number:
        print("your guess is high")
        guess_number +=1
    elif yourGues<number:
        print("your guess is low")
        guess_number +=1
    else :
        know = datetime.datetime.now()
        know_timer = know-now
        print("your guess is correct")
        guess_number +=1
        print(guess_number,"guess")
        print(know_timer.seconds,"seconds")
        break