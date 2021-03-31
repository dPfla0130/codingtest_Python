# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    min_value = sum(A[0:2]) / 2
    min_index = 0
    for i in range(len(A)):
        try:
            print(A[i], A[i+1], A[i+2])
            if min_value > (A[1 + i] + A[i]) / 2:
                min_value = (A[1 + i] + A[i]) / 2
                min_index = i

            if min_value > (A[2 + i] + A[1 + i] + A[i]) / 3:
                min_value = (A[2 + i] + A[1 + i] + A[i]) / 3
                min_index = i
        except:
            break

    return min_index


if __name__ == "__main__":
    print(solution([4, 2, 2, 5, 1, 5, 8]))