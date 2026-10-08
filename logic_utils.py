"""Pure game logic for the number guessing game (no Streamlit code here)."""

DIFFICULTY_RANGES = {
    "Easy": (1, 20),
    "Normal": (1, 50),
    "Hard": (1, 100),  # FIX: was 1-50, which made Hard easier than Normal
}


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    return DIFFICULTY_RANGES.get(difficulty, (1, 100))


def parse_guess(raw: str, low: int = None, high: int = None):
    """
    Parse user input into an int guess.

    If low and high are given, the guess must fall inside that range.
    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        # FIX: decimals like "3.9" are rejected instead of silently truncated
        value = int(raw.strip())
    except ValueError:
        return False, None, "Please enter a whole number."

    # FIX: out-of-range guesses are rejected
    if low is not None and high is not None and not (low <= value <= high):
        return False, None, f"Your guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).

    outcome is one of: "Win", "Too High", "Too Low"
    """
    # FIX: both values are always ints now, so the TypeError/string
    # comparison fallback is gone.
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"  # FIX: hints were swapped
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update score based on outcome and attempt number.

    attempt_number is 1-based: 1 means this was the player's first guess.
    """
    if outcome == "Win":
        # FIX: a first-try win now earns 100 (was 70 due to an off-by-one)
        points = max(10, 100 - 10 * (attempt_number - 1))
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        # FIX: every wrong guess costs 5; "Too High" no longer earns points
        return current_score - 5

    return current_score