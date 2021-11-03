print("Welcome from Quiz Game")

game = input("Do you want to play ? : ")

if game.lower() == "yes":
    print("Let's play!!!")
else:
    print("Okay byeee!!!")
    quit()

score = 0


question1 = input("What does CPU stand for ? : ")
if question1.lower() == "central processing unit":
    print("Corret!!!")
    score += 1
else:
    print("Incorrect!!!")

question3 = input("What does GPU stand for ? : ")
if question3.lower() == "graphic processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect!!!")

question4 = input("What does RAM stand for ? : ")
if question4.lower() == "random access memory":
    print("Correct!!!")
    score += 1
else:
    print("Incorrect!!!")

question3 = input("What does PSU stnad for ? : ")
if question3.lower() == "power supply":
    print("Correct!!!")
    score += 1
else:
    print("Incorrect!!!")

print("Thanks for playing!")
print("You got",score,"question correct!")
print("You got",int(score)/4*100,"% ")
#Gittest