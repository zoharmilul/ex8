import nonogram

def test_can_fill():
    assert nonogram._can_fill([0,0,0,0,0],2,0) == True
    assert nonogram._can_fill([1, 1, 0, 0, 0], 2, 3) == True
    assert nonogram._can_fill([0, 0, 0, 0, 0], 7, 0) == False
    assert nonogram._can_fill([1, 1, 1, 0, 0], 1, 4) == True
    assert nonogram._can_fill([1,1,1,1,0], 2, 0) == False
    assert nonogram._can_fill([1, 1, 0, 0, 0], 1, 2) == False

def test_constraint():
    assert nonogram.constraint_satisfactions(3, [1]) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert nonogram.constraint_satisfactions(3, [2]) == [[1, 1, 0], [0, 1, 1]]
    assert nonogram.constraint_satisfactions(3, [1,1]) == [[1, 0, 1]]
    assert nonogram.constraint_satisfactions(4, [1,1]) == [[1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1]]
    assert nonogram.constraint_satisfactions(5, [2,1]) == [[1, 1, 0, 1, 0], [1, 1, 0, 0, 1], [0, 1, 1, 0, 1]]
    assert nonogram.constraint_satisfactions(2,[3]) == []

def test_row_variation():
    assert nonogram.row_variations([1, 1, -1, 0], [3]) == [[1, 1, 1, 0]]
    assert nonogram.row_variations([-1, -1, -1, 0], [2]) == [[1, 1, 0, 0], [0, 1, 1, 0]]
    assert nonogram.row_variations([-1, 0, 1, 0, -1, 0], [1, 1]) == [[1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0]]
    assert nonogram.row_variations([-1, -1, -1], [1]) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert nonogram.row_variations([0, 0, 0], [1]) == []
    assert nonogram.row_variations([0, 0, -1, 1, 0], [3]) == []
    assert nonogram.row_variations([0, 0, -1, 1, 0], [2]) == [[0, 0, 1, 1, 0]]
    assert nonogram.row_variations([0, 0, 1, 1, 0], [2]) == [[0, 0, 1, 1, 0]]
    assert nonogram.row_variations([0, 0, -1, -1], [5]) == []
