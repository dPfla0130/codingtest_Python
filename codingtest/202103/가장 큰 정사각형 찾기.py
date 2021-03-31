def solution(board):
    n = len(board[0])
    m = len(board)
    answer = 0
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                continue
            if board[i][j] != 0:
                board[i][j] = min(board[i - 1][j - 1], min(board[i - 1][j], board[i][j - 1])) + 1
    for i in range(m):
        answer = max(answer, max(board[i]))

    return answer ** 2


if __name__ == "__main__":
    print(solution([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))