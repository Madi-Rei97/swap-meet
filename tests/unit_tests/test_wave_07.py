import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#@pytest.mark.skip
def test_swap_best_by_category():
    # Arrange
    # me
    item_a = Decor(age=5)
    item_b = Electronics(age=4)
    item_c = Decor(age=1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=0)
    item_e = Decor(age=2)
    item_f = Clothing(age=5)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other_vendor=jesse,
    )

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_c in jesse.inventory
    assert item_d in tai.inventory
