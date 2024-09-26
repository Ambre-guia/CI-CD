from inc_dec import increment, decrement

def test_increment():
    assert increment(1) == 2, "Test failed: increment(1) should return 2"
    assert increment(-1) == 0, "Test failed: increment(-1) should return 0"
    assert increment(0) == 1, "Test failed: increment(0) should return 1"
    print("All increment tests passed!")

def test_decrement():
    assert decrement(1) == 0, "Test failed: decrement(1) should return 0"
    assert decrement(-1) == -2, "Test failed: decrement(-1) should return -2"
    assert decrement(0) == -1, "Test failed: decrement(0) should return -1"
    print("All decrement tests passed!")

if __name__ == '__main__':
    test_increment()
    test_decrement()
