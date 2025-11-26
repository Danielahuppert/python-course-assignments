import pytest
from rock_paper_scissors_logic import determine_winner


def test_tie_cases():
    assert determine_winner('rock', 'rock') == "It's a tie"
    assert determine_winner('paper', 'paper') == "It's a tie"
    assert determine_winner('scissors', 'scissors') == "It's a tie"


@pytest.mark.parametrize('player,computer', [
    ('rock', 'scissors'),
    ('scissors', 'paper'),
    ('paper', 'rock'),
])
def test_player_wins(player, computer):
    assert determine_winner(player, computer) == 'Player wins'


@pytest.mark.parametrize('player,computer', [
    ('scissors', 'rock'),
    ('paper', 'scissors'),
    ('rock', 'paper'),
])
def test_player_loses(player, computer):
    assert determine_winner(player, computer) == 'Computer wins'


@pytest.mark.parametrize('bad_player,bad_computer', [
    ('', 'rock'),
    ('lava', 'rock'),
    ('rock', ''),
    ('rock', 'water'),
    (None, 'paper'),
])
def test_invalid_input(bad_player, bad_computer):
    with pytest.raises(ValueError):
        determine_winner(bad_player, bad_computer)
