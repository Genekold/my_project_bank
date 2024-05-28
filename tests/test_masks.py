import pytest

from src.masks import mask_card, mask_bank_account

def test_mask_card():
    assert mask_card("1234098765432567") == "1234 09** **** 2567"

    assert mask_card("78454537889")

    with pytest.raises(TypeError):
        mask_card(123231321231)



def test_mask_bank_account():
    assert mask_bank_account("12345678901234567890") == "**7890"

    with pytest.raises(TypeError):
        mask_bank_account(123231321231)