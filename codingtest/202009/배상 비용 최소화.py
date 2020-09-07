import heapq

def solution(no, works):
    result = 0

    #max heap으로 구현하기 위해 -1을 곱해준다 ==> 순서가 반대로 바뀜
    for i in range(len(works)):
        works[i] *= -1
    heapq.heapify(works)
    while no > 0:
        heapq.heappush(works, heapq.heappop(works)+1)
        #만약 일이 더 남아있지 않다면 0을 반환
        if works[0] == 0:
            return 0
        no -= 1

    for i in works:
        result += i**2

    return result

if __name__=="__main__":
    works = [3,3,3]
    N = 8
    print(solution(N, works))
