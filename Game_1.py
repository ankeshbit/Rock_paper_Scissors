import random
import time
print("rock🧱 defeat scissor✂ \n")
print("scissor✂  defeat paper📄\n ")
print("paper📄 defeat rock🧱\n")

time.sleep(2)
name = input("Please enter your name :- ")
age = int(input("Enter your age :- "))

if(age>60):
  print(f"{age} seems unlikely.{name} enter your real age . ")
        
elif(age<=15):
  print(f"{name} is not eligible to play this game.")
  
else:
  play_again = "yes"
  while play_again == "yes":
    i=1
    user_score = 0
    com_score = 0
    a = 0
    print("Game will start in")
    for a in range(5,0,-1):
      print(f"{a}")
      time.sleep(1)
    print("\nNew game begins.......\n")
    print(f"{name}🧑 has 5 chances to play\n")
    print("Please enter rock🧱, paper📄 or scissor✂ \n")
    while(i <= 5):
        win_messages = ["Great job!", "You're on fire! 🔥", "Well played!", "Victory! 🏆"]
        loss_messages = ["Oops!", "You got outplayed 💀", "Try again!", "Close one!"]

        u_input = input(f"Round {i} Enter your choice : \n")
        use_input = u_input.lower()
        user_input = use_input.strip()
        
        list = ["rock" , "paper" , "scissor"]
        com_input = random.choice(list)
        
        if(user_input not in list):
          print("Invalid choice\tselect your input from \"rock🧱\",\"paper📄\" and \"scissor✂\"")
        
        else:
          com_input = random.choice(list)
          if(user_input == "rock" and com_input == "scissor"):
            print(f"{name}🧑 chose {user_input} and computer💻 chose {com_input}\n{name} won🏆")
            print(random.choice(win_messages))
            user_score += 1 
        
          elif(user_input == "scissor" and com_input == "paper"):
            print(f"{name}🧑 chose {user_input} and computer💻 chose {com_input}\n{name} won🏆")
            print(random.choice(win_messages))
            user_score += 1 
        
          elif(user_input == "paper" and com_input == "rock"):
            print(f"{name}🧑 chose {user_input} and computer💻 chose {com_input}\n{name} won🏆")
            print(random.choice(win_messages))
            user_score += 1 
        
          elif (user_input == "scissor" and com_input == "scissor"):
            print(f"{name}🧑 selected {u_input} and computer💻 selected {com_input}\nMatch tie🤝")
            
          elif(user_input == "rock" and com_input == "rock"):
            print(f"{name}🧑 selected {u_input} and computer💻 selected {com_input}\nMatch tie🤝")
        
          elif(user_input == "paper" and com_input == "paper"):
            print()
            print(f"{name}🧑 selected {u_input} and computer💻 selected {com_input}\nMatch tie🤝")
        
          else:
            print()
            print(f"{name}🧑 chose {user_input} and computer💻 chose {com_input}\n{name} lost⚰")
            print(random.choice(loss_messages))
            com_score += 1 
        print()
        i+=1
    
    print(f"{name}🧑 score is ",user_score)
    print("Computer💻 Score is " ,com_score)
    print()
    if(user_score > com_score):
      print()
      print("YOU WON🥇")
    
    elif(user_score == com_score):
      print()
      print("MATCH TIE🤝")
    
    else:
      print()
      print("YOU LOST⚰")

    play_again = input("\n Do you want to play again ?(yes/no)")
    play_again.lower().strip()
    if(play_again != "yes" or play_again != "no"):
      print("Invalid input....Will be considered as \"no\"")


print()
time.sleep(2)
print("Thank you for playing!")
print("As the developer, I truly appreciate you taking the time to experience this game. Every line of code, every")
print()
time.sleep(6)
print("design choice, and every challenge was crafted with care and passion. Your support means the world, and I")
print()
time.sleep(6)
print("hope the game brought you fun, excitement, or even a moment to escape. If you enjoyed it, please consider")
time.sleep(6)
print()
print("sharing your thoughts or feedback—it helps me grow and create even better experiences in the future. Until")
time.sleep(6)
print()
print("next time, happy gaming!")
print()
print("Please enter any feedback if you want ..reply with no if you don't want to ")
feed = input("")
print("Response saved")
print("Your feedback was \"",feed,"\"")
print()
print("Compilation finished..........................")
current_time = time.strftime("%H:%M:%S")
print("at " ,current_time,"🕛")