import random
options=["rock","paper","scissors"]
print("Rock,paper or scissors?:")

print("Enter quit if you want to stop")

while True:
    man_choice=input("").lower()
    computer_choice=random.choice(options)
    print("Computer chose ",computer_choice)
    if(man_choice=="quit"):
        break
    if(man_choice==computer_choice):
        print("It's a draw dude!!!")
        
    elif((man_choice=="rock" and computer_choice=="scissors")or(man_choice=="paper" and computer_choice=="rock")or(man_choice=="scissors" and computer_choice=="paper")):
        print("you win, HURRAY!!!!!")
    else:
        print("Computer wins!!!!")
print("Game stopped")

