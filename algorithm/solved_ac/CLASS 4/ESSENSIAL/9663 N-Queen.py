def solve_n_queen(n):
    column = [False] * n
    left_diagonal = [False] * (2 * n - 1)
    right_diagonal = [False] * (2 * n - 1)

    result = 0

    def backtrack(row):
        nonlocal result
        if row == n:
            result += 1
            return

        for col in range(n):
            if column[col] or left_diagonal[row - col + (n - 1)] or right_diagonal[row + col]:
                continue

            column[col] = left_diagonal[row - col + (n - 1)] = right_diagonal[row + col] = True
            backtrack(row + 1)
            column[col] = left_diagonal[row - col + (n - 1)] = right_diagonal[row + col] = False

    backtrack(0)
    
    return result

n = int(input())
print(solve_n_queen(n))