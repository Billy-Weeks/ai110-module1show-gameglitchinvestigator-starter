from logic_utils import check_guess, new_game_state

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_guess():
    # Regression test for the swapped-hint bug.
    # A guess that is too HIGH must tell the player to go LOWER,
    # and a guess that is too LOW must tell the player to go HIGHER.
    outcome_high, message_high = check_guess(60, 50)
    assert outcome_high == "Too High"
    assert "LOWER" in message_high

    outcome_low, message_low = check_guess(40, 50)
    assert outcome_low == "Too Low"
    assert "HIGHER" in message_low

def test_new_game_resets_state():
    # Regression test for the New Game bug: after a finished game,
    # starting a new game must reset ALL per-game state, not just
    # attempts and secret.
    fresh = new_game_state(73)

    # The status must return to "playing" so the game isn't frozen
    # at the status guard (this was the cause of being locked out).
    assert fresh["status"] == "playing"

    # The rest of the session variables must reset too.
    assert fresh["score"] == 0
    assert fresh["history"] == []
    assert fresh["attempts"] == 0

    # The secret is whatever the caller passed in.
    assert fresh["secret"] == 73

def test_fresh_game_starts_with_zero_attempts():
    # Regression test for the off-by-one attempts bug: a fresh game must
    # start with 0 attempts (it was hardcoded to 1 on first load, which
    # made the count and "Attempts left" display off by one).
    fresh = new_game_state(50)
    assert fresh["attempts"] == 0

def test_guess_compares_numerically_not_as_text():
    # Regression test for the even-attempt stringify bug. When the secret was
    # turned into a string, comparisons fell back to text: "9" > "10" is True
    # lexicographically, so guessing 9 against secret 10 wrongly read "Too High".
    # With integer comparison, 9 vs 10 must be "Too Low" -> go HIGHER.
    outcome, message = check_guess(9, 10)
    assert outcome == "Too Low"
    assert "HIGHER" in message
