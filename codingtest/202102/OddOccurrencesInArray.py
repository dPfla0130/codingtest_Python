# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections
def solution(A):
    # write your code in Python 3.6
    c = collections.Counter(A)
    for key, value in c.items():
        if value%2==1:
            return key

if __name__ == "__main__":
    print(solution([9, 3, 9, 3, 9, 7, 9]))