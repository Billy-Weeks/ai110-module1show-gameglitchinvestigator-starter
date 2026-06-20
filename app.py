import random
import streamlit as st

from logic_utils import check_guess, new_game_state

def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# Seed a fresh game on first load. Reuse new_game_state (the same source of
# truth as the New Game handler) so attempts starts at 0 — it was hardcoded
# to 1 here, which made the count and "Attempts left" display off by one.
# The guard keeps state persisting across Streamlit reruns.
if "attempts" not in st.session_state:
    fresh = new_game_state(random.randint(low, high))
    st.session_state.secret = fresh["secret"]
    st.session_state.attempts = fresh["attempts"]
    st.session_state.score = fresh["score"]
    st.session_state.status = fresh["status"]
    st.session_state.history = fresh["history"]

st.subheader("Make a guess")

# BUG: The guess input and Submit button were separate widgets. In Streamlit,
# pressing Enter in a text_input only re-runs the script without "clicking" the
# button, so the guess was never processed on Enter (no hint appeared), and the
# button could act on a not-yet-committed value, making guesses lag by one entry.
# FIX: Wrap the input + submit in a st.form so pressing Enter OR clicking the
# button submits atomically with the current value. New Game and Show hint stay
# outside the form so they keep reacting immediately instead of waiting for a
# form submit.
with st.form("guess_form"):
    raw_guess = st.text_input(
        "Enter your guess:",
        key=f"guess_input_{difficulty}"
    )
    submit = st.form_submit_button("Submit Guess 🚀")

col1, col2 = st.columns(2)
with col1:
    new_game = st.button("New Game 🔁")
with col2:
    show_hint = st.checkbox("Show hint", value=True)

# FIXME: Where New Game Bug begins
if new_game:
    fresh = new_game_state(random.randint(1, 100))
    st.session_state.secret = fresh["secret"]
    st.session_state.attempts = fresh["attempts"]
    st.session_state.score = fresh["score"]
    st.session_state.status = fresh["status"]
    st.session_state.history = fresh["history"]
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        outcome, message = check_guess(guess_int, st.session_state.secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

# BUG: These status displays were rendered ABOVE the `if submit:` block that
# updates attempts/score/history. Since Streamlit runs the script top-to-bottom
# in a single pass, they showed the PREVIOUS run's values — a one-step lag after
# each guess.
# FIX: Render them AFTER the submit processing so they reflect the just-updated
# state. The form has to stay above (it must render to capture the guess); only
# the read-only displays move down here.
st.info(
    f"Guess a number between 1 and 100. "
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
