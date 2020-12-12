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
            row = _unfill_row(row, value, num)
    return options_list


def _can_fill(row , value , ind):
    return ind <= len(row) - value and row[ind] == 0 and row[ind - 1] != 1


def _unfill_row(row, value, ind):
    for num in range(value):
        row[ind] = EMPTY
        ind += 1
    return row


def _fill_row(row, value, ind):
    if value > len(row):
        return row
    if ind > len(row) - value:
        return row
    for num in range(value):
        row[ind] = FILLED
        ind += 1
    return row
print(constraint_satisfactions(3, [1]))
print(constraint_satisfactions(3, [2]))
print(constraint_satisfactions(3, [1,1]))
print(constraint_satisfactions(4, [1,1]))
print(constraint_satisfactions(5, [2,1]))
