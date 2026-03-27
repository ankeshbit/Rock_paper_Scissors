import random
import time

print("rock🧱 defeat scissor✂ \n")
print("scissor✂  defeat paper📄\n")
print("paper📄 defeat rock🧱\n")

time.sleep(2)

name = input("Please enter your name :- ")
age = int(input("Enter your age :- "))

if age > 60:
    print(f"{age} seems unlikely. {name}, enter your real age.")

elif age <= 15:
    print(f"{name} is not eligible to play this game.")

else:
    play_again = "yes"

    while play_again == "yes":
        i = 1
        user_score = 0
        com_score = 0

        print("Game will start in")
        for a in range(5, 0, -1):
            print(f"{a}")
            time.sleep(1)

        print("\nNew game begins.......\n")
        print(f"{name}🧑 has 5 chances to play\n")
        print("Please enter rock🧱, paper📄 or scissor✂ \n")

        choices = ["rock", "paper", "scissor"]

        while i <= 5:
            win_messages = ["Great job!", "You're on fire! 🔥", "Well played!", "Victory! 🏆"]
            loss_messages = ["Oops!", "You got outplayed 💀", "Try again!", "Close one!"]

            u_input = input(f"Round {i} Enter your choice : \n")
            user_input = u_input.lower().strip()

            if user_input not in choices:
                print("Invalid choice. Select from \"rock🧱\", \"paper📄\" and \"scissor✂\"")
                continue

            com_input = random.choice(choices)

            if user_input == com_input:
                print(f"{name}🧑 selected {user_input} and computer💻 selected {com_input}\nMatch tie🤝")

            elif (user_input == "rock" and com_input == "scissor") or \
                 (user_input == "scissor" and com_input == "paper") or \
                 (user_input == "paper" and com_input == "rock"):

                print(f"{name}🧑 chose {user_input} and computer💻 chose {com_input}\n{name} won🏆")
                print(random.choice(win_messages))
                user_score += 1

            else:
                print(f"{name}🧑 chose {user_input} and computer💻 chose {com_input}\n{name} lost⚰")
                print(random.choice(loss_messages))
                com_score += 1

            print()
            i += 1

        print(f"{name}🧑 score is {user_score}")
        print(f"Computer💻 Score is {com_score}")
        print()

        if user_score > com_score:
            print("YOU WON🥇")
        elif user_score == com_score:
            print("MATCH TIE🤝")
        else:
            print("YOU LOST⚰")

        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()

        if play_again not in ["yes", "no"]:
            print("Invalid input... considered as \"no\"")
            play_again = "no"

print()
print("Please enter any feedback if you want... reply with 'no' if you don't want to")
feed = input("")
print("Response saved")
print(f"Your feedback was \"{feed}\"")
print()
print("Compilation finished..........................")

current_time = time.strftime("%H:%M:%S")
print("at", current_time, "🕛")