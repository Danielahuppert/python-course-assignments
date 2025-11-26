"""
Pure business logic for Rock-Paper-Scissors.
Provides determine_winner(player_choice, computer_choice) -> str
"""
from __future__ import annotations

VALID_CHOICES = ("rock", "paper", "scissors")


def determine_winner(player_choice: str, computer_choice: str) -> str:
    """Determine the winner between player and computer.

    Args:
        player_choice: one of 'rock', 'paper', 'scissors' (case-insensitive)
        computer_choice: one of 'rock', 'paper', 'scissors' (case-insensitive)

    Returns:
        'Player wins', 'Computer wins', or "It's a tie".

    Raises:
        ValueError: if either choice is invalid.
    """
    if player_choice is None or computer_choice is None:
        raise ValueError("Both choices must be provided")

    p = player_choice.strip().lower()
    c = computer_choice.strip().lower()

    if p not in VALID_CHOICES:
        raise ValueError(f"Invalid player choice: {player_choice}")
    if c not in VALID_CHOICES:
        raise ValueError(f"Invalid computer choice: {computer_choice}")

    if p == c:
        return "It's a tie"

    # mapping: choice -> choice it beats
    wins_over = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock',
    }

    if wins_over[p] == c:
        return 'Player wins'
    else:
        return 'Computer wins'
