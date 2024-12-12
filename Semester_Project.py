
# Using a dictionary for scores
scores = {"player1": 0, "player2": 0}

# Helper function to determine the winner
def determine_winner(player1, player2):
    if player1 == player2:
        return "draw"
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "scissors" and player2 == "paper"):
        return "player1"
    else:
        return "player2"

# Main game function
def play_game(scores):
    player1 = input("Player 1, enter either rock, paper, or scissors: ").lower()
    player2 = input("Player 2, enter either rock, paper, or scissors: ").lower()

    result = determine_winner(player1, player2)

    if result == "draw":
        print("It's a draw!")
    elif result == "player1":
        print("Player 1 wins this round!")
        scores["player1"] += 1
    else:
        print("Player 2 wins this round!")
        scores["player2"] += 1

    return scores

# Loop for multiple rounds
def start_game():
    while True:
        scores = play_game(scores)
        print(f"Current score - Player 1: {scores['player1']} Player 2: {scores['player2']}")
        
        if scores["player1"] == 2:
            print("Player 1 wins the game!")
            break
        elif scores["player2"] == 2:
            print("Player 2 wins the game!")
            break

start_game()

