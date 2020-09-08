#정확도 통과, 효율성 실패
import heapq
def solution(healths, items):
    answer = []
    for i in range(len(items)):
        items[i].append(i)
    # 공격력이 높은 기준으로 내림차순
    items = sorted(items, key=lambda x: (x[0], x[1]), reverse=True)
    # 체력이 낮은 순으로 오름차순
    healths.sort()
    for i in range(len(healths)):
        heap = []
        for j in range(len(items)):
            if healths[i]-items[j][1] >= 100:
                heap.append((items[j][0], items[j][2]))
        if heap:
            heapq._heapify_max(heap)
            answer.append(heap[0][1]+1)
            # 삭제할 아이템을 items 배열에서 찾아 지운다(sort로 인해 배열 순서가 달라졌으므로 공격력 기준으로 찾는다)
            for k in range(len(items)):
                if items[k][0]==heap[0][0]:
                    del items[k]
                    break

    answer.sort()
    return answer

if __name__=="__main__":
    #print(solution(healths=[150, 160, 140], items=[[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60]]))
    #print(solution(healths=[150, 140, 160], items=[[60, 60], [50, 50], [40, 40], [30, 30], [20, 20], [10, 10]]))
    print(solution(healths=[1900, 130, 500], items=[[30,100],[500,30],[600,400]]))
