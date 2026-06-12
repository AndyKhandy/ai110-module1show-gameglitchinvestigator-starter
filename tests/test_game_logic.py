import sys
from unittest.mock import MagicMock

# Prevent Streamlit from executing module-level UI calls during import.
# selectbox must return a valid difficulty string; columns must unpack correctly.
_mock_st = MagicMock()
_mock_st.sidebar.selectbox.return_value = "Normal"
_mock_st.columns.side_effect = lambda n: [MagicMock() for _ in range(len(n) if isinstance(n, (list, tuple)) else n)]
sys.modules.setdefault("streamlit", _mock_st)

from logic_utils import get_range_for_difficulty
from logic_utils import check_guess
from logic_utils import parse_guess


def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_hard_range_larger_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_parse_guess_empty_and_whitespace():
    """Empty string and whitespace-only input should both fail with the same message."""
    ok_empty, _, msg_empty = parse_guess("")
    ok_ws, _, msg_ws = parse_guess("   ")
    assert ok_empty is False
    assert ok_ws is False
    assert msg_empty == "Enter a guess."
    assert msg_ws == "Enter a guess."


def test_parse_guess_negative_number():
    """Negative integers are valid to parse; check_guess should then classify them correctly."""
    ok, value, err = parse_guess("-7")
    assert ok is True
    assert value == -7
    assert err is None
    outcome, _ = check_guess(-7, 50)
    assert outcome == "Too Low"


def test_parse_guess_non_numeric_string():
    """Alphabetic and symbol strings that cannot be cast to int should fail gracefully."""
    for bad in ("abc", "!@#", "12abc", "one"):
        ok, value, msg = parse_guess(bad)
        assert ok is False, f"Expected failure for input {bad!r}"
        assert value is None
        assert msg == "That is not a number."
