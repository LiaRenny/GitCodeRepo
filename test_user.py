# test_user.py
from user import User

def test_can_vote_true():
    user = User("Alice", 20)
    assert user.can_vote() is True

def test_can_vote_false():
    user = User("Bob", 16)
    assert user.can_vote() is False

def test_can_vote_edge():
    user = User("Charlie", 18)
    assert user.can_vote() is True