import os
import sys

# Make logic_utils.py (in the project root) importable from the test/ folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic_utils import check_guess


# --- Starter tests ---
# check_guess returns (outcome, message), so each test unpacks the tuple
# and checks the outcome.

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the swapped-hint bug ---
# The original code returned the right outcome but the wrong message,
# so these tests check the message too.

def test_too_high_message_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message