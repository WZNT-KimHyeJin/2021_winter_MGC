n=5
grid=[
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
]

def GetnumOfGold(row, col_s, col_e):
    num_of_gold =0

    for col in  range(col_s,col_e + 1):
        num_of_gold += grid[row][col]
    return num_of_gold

    max_gold =0

    for row in range(0,n):
        for col in range(0,n):
            if col + 2 >= n : continue

            num_of_gold = GetnumOfGold(row,col,col+2)

            max_gold = max(max_gold,num_of_gold)

    print(max_gold)