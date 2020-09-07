import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    #정렬되어 있는 리스트에서 새로운 원소를 삽입할 때 가장 빠른 정렬 자료구조
    #heap, priority queue
    try:
        while scoville[0] < K:
            fir = heapq.heappop(scoville)
            sec = heapq.heappop(scoville)
            heapq.heappush(scoville, fir + sec*2)
            answer += 1
    except:
        return -1
    return answer

if __name__=="__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))
