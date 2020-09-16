from itertools import combinations
def solution(s):
    stack = []

    for ch in s:
        while stack and stack[-1] < ch:
            stack.pop()
        stack.append(ch)
    answer = ''.join(stack)
    return answer



if __name__ == "__main__":
    print(solution(s = "xyb"))