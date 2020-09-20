def solution(seat):
    seat.sort()
    li = [seat[0]]
    for i in seat:
        if li[-1] != i:
            li.append(i)

    return len(li)

if __name__ == "__main__":
    print(solution(seat=[[1,1],[2,1],[1,2],[3,4],[2,1],[2,1]]))
