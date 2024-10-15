# Fixture Python - Similar to precondition and postcondition

import pytest


@pytest.fixture()
def is_married():
    return True


def test_I_need_confirmation(is_married):
    assert is_married == True