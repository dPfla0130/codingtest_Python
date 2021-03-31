def climbingStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    pibo1 = 2
    pibo2 = 3
    pibo3 = 0
    for i in range(4, n+1):
        pibo3 = pibo1 + pibo2
        pibo1 = pibo2
        pibo2 = pibo3
    return pibo3







if __name__ == "__main__":
    print(climbingStairs(7))

