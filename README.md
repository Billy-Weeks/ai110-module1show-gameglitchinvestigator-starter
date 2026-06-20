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

- [ ] Describe the game's purpose.
      The game is a basic "Guess the secret number game" where a user enters a number 1-100 and the game tells the user (if hints are enabled) if they need to "Go HIGHER!" or "Go LOWER!" on their next guess. Each difficulty has a certain number of attempts allowed and range of numbers the secret number will be chosen from
- [ ] Detail which bugs you found.
      --Found the bug where after a win/loss of a game, a new game could not be started despite the attempts and secret number being reset.
      --Also, found a bug where the wrong hint message was being sent to the user. They were told to guess higher, even though their previous guess was greater than the secret number already or guess lower when their previous guess was already too low.
      --The bug where a new spin up of the game already had the user with 1 attempt being recorded even though no guess was made yet.
      --Enter/submit button press did not update "history" until next enter or submit was pressed
- [ ] Explain what fixes you applied.
      -- Changed the order of the code so that the enter press updated the score, attempts left and history at time of press instead of next turn
      -- Adjusted the hint messages to accurately describe where the guess was in relation to the secret number
      -- Fixed the line of code which set the session state of attempts automatically to 1 at first spin up of game
      -- Added lines of code so that ALL session state variables were reset at start of New Game, instead of just the secret number and attempts. (this
      included the status variable which was stuck at won/loss causing the New Game button to not work)
## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User starts up the game and is able to make a guess, or select a different difficutly
2. User enters a guess of 65, presses enter/submit guess button
3. If hints enabled: Game returns "Go HIGHER!", otherwise no message
4. Score and "Attempts left" are updated.
5. User enters a guess of 100
6. Game returns "Go LOWER!"
7. Score and "Attempts left" are updated
8. Once correct number is guessed OR number of attempts runs out, game ends with appropriate message and score.
9. New game button is selected
10. Score, secret number, attempts left are all reset.
11. New game begins

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
