import pytest

from utils.statsbomb_wrappers import PitchDim


def test_pitch_dims():
    assert PitchDim.DEF_GOAL_LPOST.value == (0, 36)
    assert PitchDim.DEF_GOAL_RPOST == (0, 44)
    assert PitchDim.ATT_GOAL_LPOST == (120, 36)
    assert PitchDim.ATT_GOAL_RPOST == (120, 44)
