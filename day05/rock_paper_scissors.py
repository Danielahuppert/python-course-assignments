import random
option =["rock", "paper", "scissors"]
def determine_winner(player1_choice):
    """Determine the winner of a rock-paper-scissors game.

    Args:
        player1_choice (str): Choice of player 1 ("rock", "paper", or "scissors").
        player2_choice (str): Choice of player 2 ("rock", "paper", or "scissors").

    Returns:
        str: "Player 1 wins", "Player 2 wins", or "It's a tie".
    """
    player2_choice = random.choice(option)
    print(f"Computer chose: {player2_choice}")

    if player1_choice == player2_choice:
        return "It's a tie"
    
    winning_combinations = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if winning_combinations[player1_choice] == player2_choice:
        return "Player 1 wins"
    else:
        return "Player 2 wins"

if __name__ == "__main__":
    import sys
    player_choice = sys.argv[1]
    print(determine_winner(player_choice))
