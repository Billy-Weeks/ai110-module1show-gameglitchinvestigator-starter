def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# FIX: Imported logic from app.py and refactored using agent mode
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# FIX: New Game previously reset only attempts & secret, leaving score, history,
# and status stale. The stale "won"/"lost" status froze the new game at the
# status guard. This returns a full fresh state so every per-game field resets.
def new_game_state(secret):
    """
    Return the fresh session-state values for starting a new game.

    The caller draws the random secret and writes these values into
    st.session_state. Returns a dict of every per-game field:
    secret, attempts, score, status, history.
    """
    return {
        "secret": secret,
        "attempts": 0,
        "score": 0,
        "status": "playing",
        "history": [],
    }
