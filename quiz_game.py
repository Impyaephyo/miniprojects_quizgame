print("Welcome from Quiz Game")

game = input("Do you want to play ? : ")

if game.lower() == "yes":
    print("Let's play!!!")
else:
    print("Okay byeee!!!")

question = input("What does CPU stand for ? : ")
if question.lower() == "central processing unit":
    print("Corret!!!")
else:
    print("Incorrect!!!")

question1 = input("What does GPU stand for ? : ")
if question1.lower() == "graphic processing unit":
    print("Correct")
else:
    print("Incorrect!!!")

question2 = input("What does RAM stand for ? : ")
if question2.lower() == "random access memory":
    print("Correct!!!")
else:
    print("Incorrect!!!")

print("Thanks for playing!")
#Gittest