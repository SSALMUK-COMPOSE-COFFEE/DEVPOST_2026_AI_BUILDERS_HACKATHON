from auth import next_free_slot


def test_a_next_free_slot_start_free():
    assert next_free_slot({1, 2}, 3) == 3


def test_next_free_slot_skips_taken():
    assert next_free_slot({1, 2, 3}, 1) == 4


def test_next_free_slot_empty():
    assert next_free_slot(set(), 0) == 0
