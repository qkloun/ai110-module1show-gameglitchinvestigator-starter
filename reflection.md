# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- - The game looked perfectly fine, the UI was clean, simple and without any defects. It also had working theme features in the website same with the new game and submit guess buttons. However I did notice that there is a missing attempt from the 8 that was supposed to be guaranteed.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

- - The hints were backwards.
- - There is an attempt missing from the game.
- - Hard being easier than Normal
- - New game doesn't refresh game state
- - Wrong answers can increase points

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| "75" | "Should've said go LOWER" | Said go HIGHER| none |
| none|"8 attempts available to guess the number"| "session starts with one attempt used"| none |
| "New Game" | "Expected to for the game to reset the games status"| "After losing, I clicked New Game, but it still said 'Game over' and wouldn't accept guesses"| none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
