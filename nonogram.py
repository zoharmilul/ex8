import copy
FILLED = 1
EMPTY = 0
UNKNOWN = -1

def constraint_satisfactions (n, blocks):
    options_list = []
    options_list += _constraint_helper(n,blocks,[0] * n,[])
    return options_list

def _constraint_helper(n, blocks , row, options_list):
    if blocks == []:
        options_list.append(row)
        return row
    if n == 0:
        return
    value = blocks[0]
    for ind in range(n):
        if _can_fill(row, value, ind):
            row = _fill_row(row, value, ind)
            _constraint_helper(n, blocks[1:], row, options_list)
        else:
            continue
    return options_list


def _can_fill(row,value,ind):
    return ind <= len(row)-value and row[ind] == 0 and row[ind-1] != 1



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