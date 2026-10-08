import random
import streamlit as st

from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)

ATTEMPT_LIMITS = {"Easy": 6, "Normal": 8, "Hard": 5}


def start_new_game(low: int, high: int):
    """Reset every piece of game state (FIX: old New Game missed most of these)."""
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0  # FIX: was 1 on first load
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []


st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")
st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")
difficulty = st.sidebar.selectbox("Difficulty", ["Easy", "Normal", "Hard"], index=1)

attempt_limit = ATTEMPT_LIMITS[difficulty]
low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# FIX: a new secret is drawn when the difficulty changes, not just on first load
if "secret" not in st.session_state or st.session_state.get("difficulty") != difficulty:
    st.session_state.difficulty = difficulty
    start_new_game(low, high)

st.subheader("Make a guess")
# Placeholder filled in after the guess is processed, so the count isn't stale
attempts_info = st.empty()

raw_guess = st.text_input("Enter your guess:", key=f"guess_input_{difficulty}")

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    start_new_game(low, high)  # FIX: uses the difficulty's range
    st.rerun()

if submit and st.session_state.status == "playing":
    ok, guess, err = parse_guess(raw_guess, low, high)

    if not ok:
        st.error(err)  # FIX: invalid input no longer costs an attempt
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess)

        # FIX: secret is always passed as an int
        outcome, message = check_guess(guess, st.session_state.secret)

        if show_hint and outcome != "Win":
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"

if st.session_state.status == "won":
    st.success(
        f"You won! The secret was {st.session_state.secret}. "
        f"Final score: {st.session_state.score}. Start a new game to play again."
    )
elif st.session_state.status == "lost":
    st.error(
        f"Out of attempts! The secret was {st.session_state.secret}. "
        f"Score: {st.session_state.score}. Start a new game to try again."
    )

# FIX: range now matches difficulty, and the count reflects the latest guess
attempts_info.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")