import random

while True:
    player = input("rock, paper, or scissors? (or 'quit'): ").lower()
    if player == 'quit':
        break

    if player not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please try again.")
        continue

    computer = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer}")

    if player == computer:
        print("Tie!")
    elif (player == 'rock' and computer == 'scissors') or (player == 'scissors' and computer == 'paper') or (player == 'paper' and computer == 'rock'):
        print("You win!")
    else:
        print("Computer wins!")
