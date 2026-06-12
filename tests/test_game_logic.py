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
