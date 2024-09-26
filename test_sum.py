from sum import add

def test_add():
    """Tests for the add function."""
    assert add(2, 3) == 5, "Test failed: 2 + 3 should be 5"
    assert add(-1, 1) == 0, "Test failed: -1 + 1 should be 0"
    assert add(0, 0) == 0, "Test failed: 0 + 0 should be 0"
    
    print("All tests passed!")

if __name__ == '__main__':
    test_add()
