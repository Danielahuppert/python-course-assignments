# day05 — Rock Paper Scissors

What the game does

- This repository contains a simple Rock-Paper-Scissors game where you play against the computer.
- The computer picks its choice at random and the program determines the winner.

Files of interest

- `rock_paper_scissors.py` — small script that runs the game from the command line. It expects a single argument for the player's choice (e.g. `rock`, `paper`, or `scissors`). The script prints the computer's choice and the outcome.
- `rock_paper_scissors_logic.py` — pure business logic implementing `determine_winner(player_choice, computer_choice)` used by tests and other code.
- `tests/test_rock_paper_scissors.py` — pytest test suite covering tie, player wins, player loses, and invalid input cases.

How to run the game

Open a terminal, change to the `day05` folder, and run:

```powershell
python rock_paper_scissors.py rock
```

Replace `rock` with `paper` or `scissors` as desired. The script prints what the computer chose and the result.

How to run the tests

Install `pytest` if you don't already have it:

```powershell
python -m pip install pytest
```

Run the tests from the repository root or from the `day05` folder:

```powershell
# from repository root
python -m pytest day05/tests -q

# or from the day05 folder
python -m pytest tests -q
```

Dependencies

- The game itself uses only Python's standard library (no extra dependencies).
- For running tests you will need `pytest` (only required for testing).

Notes

- The game script expects a valid choice; the logic module validates inputs and tests cover invalid inputs.
- If you'd like, I can make the command-line game accept interactive input (prompting) instead of a single argument, or add a small README example of typical output.
