# Using a dictionary for scores to track each player's score
scores = {"player1": 0, "player2": 0}

# Helper function to determine the winner of the round
def determine_winner(player1, player2):
    # Check if both players chose the same move (draw)
    if player1 == player2:
        return "draw"
    # Check if player1's move beats player2's move
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "scissors" and player2 == "paper"):
        return "player1"  # player1 wins
    else:
        return "player2"  # player2 wins

# Function to get valid input from a player (rock, paper, or scissors)
def get_valid_move(player_number):
    # Loop until the player enters a valid move
    while True:
        move = input(f"Player {player_number}, enter either rock, paper, or scissors: ").lower()
        if move in ["rock", "paper", "scissors"]:
            return move
        else:
            print("Invalid input! Please enter rock, paper, or scissors.")

# Main game function that processes one round of the game
def play_game(scores):
    # Get valid moves from both players
    player1 = get_valid_move(1)
    player2 = get_valid_move(2)

    # Call the helper function to determine the winner of the round
    result = determine_winner(player1, player2)

    # Display the result of the round
    if result == "draw":
        print("It's a draw!")  # If it's a draw, notify both players
    elif result == "player1":
        print("Player 1 wins this round!")  # If player 1 wins, update score and display message
        scores["player1"] += 1  # Increment player 1's score by 1
    else:
        print("Player 2 wins this round!")  # If player 2 wins, update score and display message
        scores["player2"] += 1  # Increment player 2's score by 1

    # Return the updated scores after the round
    return scores

# Loop to run multiple rounds and check for the winner of the game
def start_game():
    # Infinite loop to continue the game until one player reaches 2 points
    while True:
        # Call the play_game function and update the scores
        global scores  # Declare the global variable to modify it inside the function
        scores = play_game(scores)
        
        # Display the current score after each round
        print(f"Current score - Player 1: {scores['player1']} Player 2: {scores['player2']}")
        
        # Check if any player has won the game (reached 2 points)
        if scores["player1"] == 2:
            print("Player 1 wins the game!")  # If player 1 wins the game, announce and exit the loop
            break
        elif scores["player2"] == 2:
            print("Player 2 wins the game!")  # If player 2 wins the game, announce and exit the loop
            break

# Start the game by calling the start_game function
start_game()

