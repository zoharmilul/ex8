import nonogram

def test_can_fill():
    assert nonogram._can_fill([0,0,0,0,0],2,0) == True
    assert nonogram._can_fill([1, 1, 0, 0, 0], 2, 3) == True
    assert nonogram._can_fill([0, 0, 0, 0, 0], 7, 0) == False
    assert nonogram._can_fill([1, 1, 1, 0, 0], 1, 4) == True
    assert nonogram._can_fill([1,1,1,1,0], 2, 0) == False
    assert nonogram._can_fill([1, 1, 0, 0, 0], 1, 2) == False
