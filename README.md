# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

### Game Purpose
 
Glitchy Guesser is a number guessing game built with Streamlit. The game picks a secret number in a range set by the difficulty (Easy: 1–20, Normal: 1–100, Hard: 1–100). The player has a limited number of attempts to guess it, and after each guess the game gives a "Go HIGHER" or "Go LOWER" hint. Each wrong guess costs 5 points, and a win earns more points the fewer attempts it takes. 

### Bugs Found
 
1. **Backwards hints.** A guess above the secret said "Go HIGHER!", and a guess below it said "Go LOWER!".
2. **Secret turned into a string on even attempts.** On every second guess the secret was converted to text. The comparison then became alphabetical, so `"9" > "50"` counted as true and the hints were wrong about half the time.
3. **Missing attempt.** Attempts started at 1 instead of 0, so Normal showed 7 attempts left instead of 8.
4. **Stale attempts counter.** "Attempts left" was drawn before the latest guess was counted, so it was always one turn behind.
5. **New Game didn't fully reset.** It reset attempts and the secret but not the status, score, or history. After a win or loss, the game stayed stuck on "Game over." It also always picked the secret from 1–100, whatever the difficulty.
6. **Changing difficulty kept the old secret.** Switching from Normal to Easy could leave a secret like 87 that was impossible to guess in the 1–20 range.
7. **Hard was easier than Normal.** Hard used the range 1–50 while Normal used 1–100.
8. **Prompt always said "1 and 100",** whatever the difficulty.
9. **Scoring bugs.** A "Too High" guess on an even attempt gained 5 points instead of losing them, and an off-by-one meant a first-try win scored 70 instead of 100.
10. **Weak input handling.** Invalid input like "abc" still used up an attempt, decimals were silently cut off (3.9 became 3), and out-of-range guesses were accepted.
11. **Logic mixed with UI.** All game logic lived in `app.py`, and every function in `logic_utils.py` just raised `NotImplementedError`.

### Fixes Applied
 
- **Refactor:** Moved `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` into `logic_utils.py`. `app.py` now imports them and only handles the UI.
- **Hints:** Swapped the "Go HIGHER" and "Go LOWER" messages in `check_guess` and removed the string-comparison fallback. The secret is now always passed as an integer.
- **Game state:** Added a `start_new_game()` helper that resets the secret, attempts, score, status, and history together, using the current difficulty's range. It runs on first load, on New Game, and whenever the difficulty changes.
- **Attempts:** Attempts start at 0, invalid input no longer uses one up, and the "Attempts left" message is filled in after the guess is processed so it is always current.
- **Difficulty:** Hard now uses 1–100, and the prompt shows the real range.
- **Scoring:** Every wrong guess costs 5 points, and a win earns `max(10, 100 - 10 * (attempt - 1))`, so a first-try win scores 100.
- **Input:** `parse_guess` trims spaces and rejects non-numbers, decimals, and guesses outside the range, with a clear error message for each.
- **Tests:** The starter tests compared `check_guess`'s result to a single string, but it returns `(outcome, message)`, so they were updated to unpack the pair. Two new tests check the hint *message*, because the original bug returned the right outcome with the wrong message.


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The game starts. The prompt says "Guess a number between 1 and 100. Attempts left: 8" and the score is 0.
2. User enters `abc` → error: "Please enter a whole number." No attempt is used, so attempts left stays at 8.
3. User enters `150` → error: "Your guess must be between 1 and 100." Attempts left still stays at 8.
4. User enters `40` → "Too Low", hint "📈 Go HIGHER!". Score: -5. Attempts left: 7.
5. User enters `70` → "Too High", hint "📉 Go LOWER!". Score: -10. Attempts left: 6.
6. User enters `60` → "Too Low", hint "📈 Go HIGHER!". Score: -15. Attempts left: 5.
7. User enters `63` → Win! Balloons appear and the game shows "You won! The secret was 63. Final score: 55." (A win on the 4th attempt earns 70 points, and -15 + 70 = 55.)
8. The secret stays 63 the whole game, so it doesn't change between guesses.
9. Clicking **Submit Guess** again does nothing, because the game is over.
10. User clicks **New Game** → a new secret is picked, attempts reset to 8, the score resets to 0, the history is cleared, and guessing works again.
11. User switches difficulty to **Easy** → a new game starts automatically with range 1–20 and 6 attempts.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- /Library/Frameworks/Python.framework/Versions/3.14/bin/python3.14
cachedir: .pytest_cache
rootdir: /Users/yunuskaratas/Desktop/Glitch/ai110-module1show-gameglitchinvestigator-starter/tests
plugins: anyio-4.15.1
collected 5 items                                                              

test_game_logic.py::test_winning_guess PASSED                            [ 20%]
test_game_logic.py::test_guess_too_high PASSED                           [ 40%]
test_game_logic.py::test_guess_too_low PASSED                            [ 60%]
test_game_logic.py::test_too_high_message_says_go_lower PASSED           [ 80%]
test_game_logic.py::test_too_low_message_says_go_higher PASSED           [100%]

============================== 5 passed in 0.04s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
