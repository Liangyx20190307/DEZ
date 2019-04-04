import itertools

sudoku = [[5,8,0,7,2,0,9,3,6],
          [3,2,0,8,6,0,7,1,0],
          [1,0,0,3,0,9,8,0,4],
          [0,0,0,0,7,3,0,8,0],
          [8,0,6,0,1,0,0,7,0],
          [7,5,3,0,8,0,4,0,1],
          [4,0,8,2,0,6,1,0,0],
          [0,0,5,1,0,8,2,9,3],
          [0,1,0,0,0,7,0,0,0]]

def not_done(s):
    return True in [0 in r for r in s]

def get_row(s, r):
    return s[r]

def get_column(s, c):
    return [r[c] for r in s]

def get_borders(n):
    borders = [[0,1,2],[3,4,5],[6,7,8]]
    for border in borders:
        if n in border:
            return border

def get_box(s, r, c):
    return [s[x][y] for x, y in \
            itertools.product(get_borders(r), get_borders(c))]

def get_possible(s, r, c):
    return [i for i in range(1, 10) \
                if i not in get_row(s, r) \
                and i not in get_column(s, c) \
                and i not in get_box(s, r, c)]

def go_around(s):
    ans = []
    for index_r, r in enumerate(s):
        row = []
        for index_c, c in enumerate(r):
            if 0 == c:
                maybe_ans = get_possible(s, index_r, index_c)
                row.append(maybe_ans[0] if len(maybe_ans) == 1 \
                           else 0)
            else:
                row.append(c)
        ans.append(row)
    return ans

def print_sudoku(s, msg):
    print (msg)
    for r in s:
        print (" ".join([str(c) for c in r]))
    print ("*"*18)


print_sudoku(sudoku, "initializing...")
counter = 1
while not_done(sudoku):
    sudoku = go_around(sudoku)
    print_sudoku(sudoku, "Round "+ str(counter) + " :")
    counter += 1



