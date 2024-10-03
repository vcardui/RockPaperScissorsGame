import random

# User's choice code

user_choice = int(input("What do you choose? Type = 1 for ROCK, 2 for PAPER or 3 for SCISSORS: "))

if 0 < user_choice and user_choice < 4:

  if user_choice == 1:
    print(f"You choosed ROCK, ({user_choice})")
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

  elif user_choice == 2:
    print(f"You choosed PAPER, ({user_choice})")
    print("""
        _______
    ---'    ____)___
              ______)
              _______)
            _______)
    ---.__________)
    """)

  elif user_choice == 3:
    print(f"You choosed SCISSORS, ({user_choice})")
    print("""
        _______
    ---'   ____)____
              ______)
          __________)
          (____)
    ---.__(___)
    """)

  # Computer's choice code

  computer_choice = random.randint(1,3)
  print(computer_choice)

  if computer_choice == 1:
    print(f"Computer choosed ROCK, ({computer_choice})")
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

  elif computer_choice == 2:
    print(f"Computer choosed PAPER, ({computer_choice})")
    print("""
        _______
    ---'    ____)___
              ______)
              _______)
            _______)
    ---.__________)
    """)

  elif computer_choice == 3:
    print(f"Computer choosed SCISSORS, ({computer_choice})")
    print("""
        _______
    ---'   ____)____
              ______)
          __________)
          (____)
    ---.__(___)
    """)

  # Game winning or loosing decision making code

  if user_choice == 1 and computer_choice == 3:
    print("Congratulations! You win :D")
  elif user_choice == 3 and computer_choice == 2:
    print("Congratulations! You win :D")
  elif user_choice == 2 and computer_choice == 1:
      print("Congratulations! You win :D")

  elif computer_choice == 1 and user_choice == 3:
    print("Oh no! You lose :(")
  elif computer_choice == 3 and user_choice == 2:
    print("Oh no! You lose :(")
  elif computer_choice == 2 and user_choice == 1:
      print("Oh no! You lose :(")

  elif computer_choice == 1 and user_choice == 1:
    print("Sorry, it's a tie... :|")
  elif computer_choice == 2 and user_choice == 2:
    print("Sorry, it's a tie... :|")
  elif computer_choice == 3 and user_choice == 3:
    print("Sorry, it's a tie... :|")

  #Rock wins against scissors.
  #Scissors win against paper.
  #Paper wins against rock.
else:
  print("Hey, pleace enter a valid number")