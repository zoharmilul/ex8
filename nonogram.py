import copy
FILLED = 1
EMPTY = 0
UNKNOWN = -1

def constraint_satisfactions (n, blocks):
    options_list = _constraint_helper(n,blocks,[0] * n,[])
    return options_list


def _constraint_helper(n, blocks , row, options_list):
    if not blocks:
        options_list.append(row[:])
        return row
    value = blocks[0]
    for ind in range(n):
        if _can_fill(row, value, ind):
            row = _fill_row(row, value, ind)
            _constraint_helper(n, blocks[1:], row, options_list)
            row = _unfill_row(row, value, ind)
    return options_list


def _can_fill(row,value,ind):
    return ind <= len(row)-value and row[ind] == 0 and row[ind-1] != 1

def _unfill_row(row,value, ind):
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

print(constraint_satisfactions(5, [2,1]))
print(constraint_satisfactions(10, [2,1]))