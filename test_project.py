import pytest
from project import Generate_Players, Play_match, Tournament, Player

def test_Generate_Players():
    with pytest.raises(ValueError):
        Generate_Players(7)
    with pytest.raises(ValueError):
        Generate_Players(4.4)
    with pytest.raises(ValueError):
        Generate_Players(0)
    with pytest.raises(ValueError):
        Generate_Players(-4)
    with pytest.raises(ValueError):
        Generate_Players("Cat")
    assert len(Generate_Players(8))==8
    players=Generate_Players(2)
    assert isinstance(players, list)

def test_Play_match():
    player1= Player()
    player2= Player()
    assert len(Play_match(player1, player2))==1
    assert isinstance(Play_match(player1, player2), list)


def test_Tournament():
    players = Generate_Players(4)
    assert len(Tournament(players))==1
    assert isinstance(Tournament(players), list)