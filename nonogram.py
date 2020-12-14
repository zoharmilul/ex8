import copy
FILLED = 1
EMPTY = 0
UNKNOWN = -1

def constraint_satisfactions (n, blocks):
    options_list = _constraint_helper(n, blocks, [0] * n, [], 0)
    return options_list


def _constraint_helper(n, blocks, row, options_list, ind):
    if not blocks:
        options_list.append(row[:])
        return
    value = blocks[0]
    for num in range(ind, n):
        if _can_fill(row, value, num):
            row = _fill_row(row, value, num)
            _constraint_helper(n, blocks[1:], row, options_list, num)
            row = _fill_row(row, value, num, EMPTY)
    return options_list


def _can_fill(row , value , ind):
    return ind <= len(row) - value and (row[ind] == EMPTY or row[ind] == UNKNOWN) and row[ind - 1] != FILLED

def _fill_row(row, value, ind, action = FILLED):
    if value > len(row):
        return row
    if ind > len(row) - value:
        return row
    for num in range(value):
        row[ind] = action
        ind += 1
    return row

def _check_sum(row):
    sum = 0
    for i in row:
        if i == 1:
            sum += 1
    return sum

def row_variations(row, blocks):
    pass

def _row_variations_helper(row, blocks, ind, sum ,lst):
    if _check_sum(row) == sum:
        lst.append(row[:])
        return row

    for index in range(ind, len(row)):
        for value in range(blocks[0]):
            if row[index] == UNKNOWN:
                row[index] = FILLED
                _row_variations_helper(row, blocks, index, sum, lst)
                row[index] = UNKNOWN
            if row[index] == EMPTY:
                return
            if row[index] == FILLED:
                _row_variations_helper(row, blocks, index, sum - 1, lst)

"""print(row_variations([1, 1, -1, 0], [3]))
print(row_variations([-1, -1, -1, 0], [2]))
print(row_variations([-1,0,1,0,-1],[1,1]))"""


