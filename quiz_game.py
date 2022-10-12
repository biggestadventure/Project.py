print("Welcome to my computer quiz!")
play = input("Do you want to play? ")
if play.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Oops..sorry Incorrect!")
answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Oops..sorry Incorrect!")
answer = input("What does RAM stands for? ")
if answer.lower() == "random acces memmory":
    print("Correct!")
    score += 1
else:
    print("Oops..sorry Incorrect!")
answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Oops..sorry Incorrect!")
print("You got "+ str(score)+ " questions correct!")
print("You got "+ str((score/4)*100)+"%.")
