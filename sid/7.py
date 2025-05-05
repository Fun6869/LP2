
n = int(input("Enter number of queens (n): "))


board = [[0]*n for _ in range(n)]
queen_positions = {}

columns = [False] * n
left_diagonal = [False] * (2 * n - 1)     
right_diagonal = [False] * (2 * n - 1)     
def solve(row):
    if row == n:
        return True  
    for col in range(n):
        if not columns[col] and not left_diagonal[row - col + n - 1] and not right_diagonal[row + col]:
           
            board[row][col] = 1
            queen_positions[row] = col
            columns[col] = left_diagonal[row - col + n - 1] = right_diagonal[row + col] = True

            if solve(row + 1):
                return True  
           
            board[row][col] = 0
            del queen_positions[row]
            columns[col] = left_diagonal[row - col + n - 1] = right_diagonal[row + col] = False

    return False


if solve(0):
    print("\nFinal Board:")
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\nQueen positions (row: column):", queen_positions)
else:
    print("No solution exists.")