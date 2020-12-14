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
    return ind <= len(row) - value and row[ind] == 0 and row[ind - 1] != 1


def _fill_row(row, value, ind, action = FILLED):
    if value > len(row):
        return row
    if ind > len(row) - value:
        return row
    for num in range(value):
        row[ind] = action
        ind += 1
    return row


def row_variation(row, blocks):
    option = creating_base_option(row)
    option_lst = []
    _row_variation_helper(row, blocks, 0, option_lst, option)

def _row_variation_helper(row, blocks, ind, option_lst, option):
    # base rule
    if ind == len(row):
        if option.count(FILLED):
            return option_lst
        option_lst.append(option[:])
        return option_lst
    # no more restrictions - everything filled
    if blocks == []:
        option[ind] = EMPTY
        _row_variation_helper(row, blocks, ind + 1, option_lst, option)
        option[ind] = UNKNOWN
        return option_lst

    if row[ind] == EMPTY:
        _row_variation_helper(row, blocks, ind + 1, option_lst, option)
    
    if row[ind] == FILLED:
        return filled_value(blocks, ind, option_lst, option, row)
    
    if row[ind] == UNKNOWN:
        if ind + blocks[0] == len(row):
            return filled_value(blocks, ind, option_lst, option, row)
        if ind + blocks[0] > len(row):
            return empty_value(blocks, ind, option_lst, option, row)
        
        # will the restriction fit in this place
        for i in range(ind, ind + blocks[0]):
            if row[i] == EMPTY:
                return empty_value(blocks, ind, option_lst, option, row)
        if row[ind + blocks[0]] == FILLED or option.count(FILLED) + blocks[0] > sum(blocks):
            return empty_value(blocks, ind, option_lst, option, row)
        if row[ind + blocks[0]] == EMPTY:
            return filled_value(blocks, ind, option_lst, option, row)
        
        # couple of options
        for value in [FILLED, EMPTY]:
            if value == FILLED:
                for num in range(ind, ind + blocks[0]):
                    option[num] = value
                option[ind + blocks[0]] = EMPTY
                _row_variation_helper(row, blocks[1::], ind + blocks[0] + 1, option_lst, option)
                option[ind] = UNKNOWN

            else:
                option[ind] = value
                _row_variation_helper(row, blocks, ind + 1, option_lst, option)
                option[ind] = UNKNOWN
        return option_lst

def creating_base_option(row):
    option = []
    for index in range(len(row)):
        if row[index] != -1:
            option[index] = row[index]
    return option

def filled_value(blocks, ind, option_lst, option, row):
    option[ind] = FILLED
    blocks[0] = blocks[0] - 1
    unnecessary_restriction(blocks)
    _row_variation_helper(row, blocks, ind + 1, option_lst, option)
    return option_lst


def empty_value(blocks, ind, option_lst, option, row):
    option[ind] = EMPTY
    _row_variation_helper(row, blocks, ind + 1, option_lst, option)
    return option_lst


def unnecessary_restriction(blocks):
    if blocks[0] == 0:
        blocks.remove(blocks[0])


print(_row_variation_helper([0, -1, -1, -1, 1, -1, -1, 1, 0, 0, -1, 1], [2, 3, 2], 0, [], [""] * 12))
