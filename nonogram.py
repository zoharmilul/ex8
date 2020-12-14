import copy
FILLED = 1
EMPTY = 0
UNKNOWN = -1


def constraint_satisfactions (n, blocks):
    options_list = _constraint_helper(n, blocks, [UNKNOWN] * n, [], 0)
    for option in options_list:
        change_unknown_to_empty(option)
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


def _can_fill(row, value, ind):
    return ind <= len(row) - value and (row[ind] == EMPTY or row[ind] == UNKNOWN) and row[ind - 1] != FILLED


def _fill_row(row, value, ind, action=FILLED):
    if value > len(row):
        return row
    if ind > len(row) - value:
        return row
    for num in range(value):
        row[ind] = action
        ind += 1
    return row


def _can_fill_variation(row, value, index):
    return 0 not in row[index:index+value]


def _check_sum(row, action = ""):
    sum = 0

    if action == "sum_known":
        return row.count(1)

    for i in row:
        sum += i
    return sum


def change_unknown_to_empty(row):
    for val in range(len(row)):
        if row[val] == UNKNOWN:
            row[val] = EMPTY


def row_variations(row, blocks):
    sum = _check_sum(blocks)
    options = _row_variations_helper(row, blocks, 0, sum, [])
    for option in options:
        change_unknown_to_empty(option)
    return options


def _row_variations_helper(row, blocks, ind, sum, lst):
    if not blocks:
        temp_row = row[:]
        if _check_sum(temp_row, "sum_known") == sum:
            lst.append(temp_row)
        return row
    for index in range(ind, len(row)):
        if row[index] == UNKNOWN and _can_fill_variation(row, blocks[0], index):
            _fill_row(row, blocks[0], index)
            _row_variations_helper(row, blocks[1:], index + blocks[0] + 1, sum, lst)
            _fill_row(row, blocks[0], index, UNKNOWN)
        if row[index] == EMPTY:
            continue
        if row[index] == FILLED and _can_fill_variation(row, blocks[0], index):
            _fill_row(row, blocks[0] - 1, index + 1)
            _row_variations_helper(row, blocks[1:], index + 1, sum, lst)
            _fill_row(row, blocks[0] - 1, index + 1, UNKNOWN)
    return lst
