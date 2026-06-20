# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1. Hints were not visible until "Submit Guess" was selected and then the hints were not what was expected. 
    When the number guessed was higher than the secret number, the hint was given "Too Low". Then when the number guessed was lower than the secret number, the hint given was "Too High".

2. Already have one "attempt" at start of game instead of 0. This causes "attempts allowed" to not equal "attempts left."
    ***NOTE: This only happens at initial load of game page. 
              If user selects "New Game" BEFORE end of first game, then attempts is accurate

3. "New Game" button only resets secret number, and number of attempts. However previous score doesn't change nor does the guess history. Biggest part of this bug: You cannot enter any other guesses for the new game. 
    ***NOTE: This bug only happens after previous game has finished

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input             | Expected Behavior     | Actual Behavior       | Console Output / Error |
|-------------------|-----------------------|-----------------------|------------------------|
|   guess: 9        |Message saying too low | Message says too High |       Go LOWER!        |
| (secret # = 86)   |                       |                       |                        |
|-------------------|-----------------------|-----------------------|------------------------|
|  Start up app     | No attempts recorded  |1 Attempt recorded     |       Attempts: 1      |
|--------------------------------------------------------------------------------------------|
|   Win/lose first  |                       |Score and history stay |                        |
|game. Start new one|Reset of history/score |and no new guesses     |        None            |
|                   |                       |       allowed         |                        |
|--------------------------------------------------------------------------------------------|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | ||
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | ||

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

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
