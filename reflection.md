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
 Using Claude CLI, I was able to refactor several of the bugs that I found through my initial and subsequent playthroughs of the game. During the first bug fix, Claude immediately noticed that the tests previously written in test_game_logic.py would actually cause a fail because of the return values in the tests for guesses would only return string when the function expected a tuple (outcome, message). Claude recommended to update the tests to keep the overall spirit of the original function. I verified this by double checking the code both the tests and the original function and confirmed what the agent said.

 The big bug that I was hunted for was the game not allowing a new game to start after a previous game was won or lost. Unfortunately I couldn't find exactly where/why in the code that was happening. I had an idea of about where it was, so I asked the agent to parse the code and let me know WHY this bug was happening. The agent was able to confirm that I was actually at the correct spot, I just couldn't really understand why that specific area of code was broken. 

 Honestly, I didn't run into anything blatantly "incorrect" or misleading. There was an instance during the new_game_state fix that the agent didn't move the entirety of the code to logic_utils.py but instead made a new function in that file that was then called from app.py. This did cause some confusion with the overall fix and me trying to find the fixed code. 
--- 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- 
For the first bug (messages being outputted that matched the guess correctly) I verified it was really fix by both visually seeing the messages change AND by having Claude run newly created tests specifically to target the previous bug. Claude preemptively ran its own tests before I prompted it to create a function with several tests to test whether a guess too high would output the correct message, too low would output it's message, etc. 

For each subsequent bugs, I ran through the game intentionally reproducing what previously caused the bug to appear, and each time the code worked as intended. For instance, with the new game bug, I spun up a fresh instance of the game and played the first round (cheating slightly by using the developer tools to "guess" the correct answer right away). Then I clicked "New Game" which then cleared the history, reset the attempts taken, reset the score, and produced a new secret number. Bug squashed. 

This test allowed me to see better how the code walked through the process and how the sessions were saved, which was a big reason why I couldn't see the original cause of the bug. The AI agent was super helpful in this process, however I did not use the agent to explain any of the tests as they were super straightforward. 
--- 

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
