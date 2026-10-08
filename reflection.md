# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? The game looked perfectly fine, the UI was clean, simple and without any defects. It also had working theme features in the website same with the new game and submit guess buttons. However I did notice that there is a missing attempt from the 8 that was supposed to be guaranteed.

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
- - I used Claude for this project
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 
- - AI suggested fixing the new game logic after I had missed it. After looking at it I confirmed that it was right.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
- - Claude suggested that we could add more complexities to the game such as a timer for the game so that there was more pressure and fun under pressure, which I rejected due to the fact that it wasn't a necessary feature.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- - I was able to check whether or not a bug was fixed by first running a pytest and checking appropriate values that were related to the problem and then running them manually in the website.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- - When I was figuring out the errors and trying to fix them I had to check if the hint was working properly and it wasn't. Testing let me figure out where I was making a mistake and fix that mistake as soon as possible.
- Did AI help you design or understand any tests? How?
- - I had never used pytest before so this was a very useful experience to me. AI was able to help me understand how to use pytest quickly without much effort of figuring out syntax.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit "reruns" is when a button is clicked it doesn't just click the button it completely reruns the whole code, making it so that everything is restarted from the beginning such as refreshinig the page. However sessions states are the answer to this problem as they let you keep the main information of the page (doesn't restart the whole page) once a button or function is used. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- - I don't really use pytest however I'm starting to understand why people prefer to use it rather than just using print statements every now and then to figure out where the problem is.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- - I want to focus on AI helping me out whenever I get stuck instead of being overly reliant on this tool. I need to think of it as something that can help me not do my work for me.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
- - AI is something I try not to use as often as I used to but I will try to use it as a tool that can help me in situations where I am lost and havinig difficulties understanding code or what to do. Furthermore, AI code can look clean and still be wrong, so I need to test it more often.
