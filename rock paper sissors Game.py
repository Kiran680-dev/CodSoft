#Task 4...........accept
import random
item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter your move ( Rock, Paper, scissor) :   ")

com_choice = random.choice(item_list)

print(f"User choice = {user_choice}, ....... Computer choice = {com_choice}")

if (user_choice == com_choice):
    print("Both to the same : Match Tie....please try again:)")

elif(user_choice == "Rock"):
    if(com_choice == "Paper"):
        print("Paper convers Rock = Computer win......You loose!")
    else:
        print("Rock smasher scissor = You win......Computer loose!")

elif(user_choice == "Paper"):
    if(com_choice == "Scissor"):
        print("Scissor cuts paper : Computer Win.......You loose!")
    else:
        print("paper convers Rock : You win........computer loose!")

elif(user_choice == "Scissor"):
    if(com_choice == "Paper"):
        print("scissor cuts paper : You win..........computer loose!")
    else:
        print("Rock smashes scissor : Computer win.......You loose!")
