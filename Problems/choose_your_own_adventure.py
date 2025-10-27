name = input("Type your name: ")
print("Welcome " , name , " to this adventure!")

answer = input(
    "You are at a cross road, where do you want to go? Type left or right \n").lower()

if answer == "left":
    answer =  input(
        "You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? \n")
    
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you want to talk to them (yes/no)? \n")
        
        if answer == "yes":
            print("You talked to the stranger and they gave you gold. You win!")
        elif answer == "no":
            print("You ignored the stranger and they are offended. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for tyring", name)
