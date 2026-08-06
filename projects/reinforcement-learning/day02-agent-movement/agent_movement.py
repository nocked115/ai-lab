# Computer가 Agent의 위치를 기억하고 출력하도록 만들기

grid = [
    ['S', '.', '.', '.'],
    ['.', 'X', '.', '.'],
    ['.', '.', 'X', '.'],
    ['.', '.', '.', 'G'],
]

# Agent의 현재 위치: [행, 열]
agent = [0, 0]

for row in range(len(grid)):
    output_row = []

    for col in range(len(grid[row])):
        if row == agent[0] and col == agent[1]:
            output_row.append('A')
        else:
            output_row.append(grid[row][col])

    print(' '.join(output_row))