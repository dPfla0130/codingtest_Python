def solution(a):
    answer = []
    #m은 가장 작은 풍선
    m = min(a)
    idx = a.index(m)
    #최대값으로 초기화
    lm = 1000000010
    rm = 1000000010
    
    #가장 작은 풍선 전까지 최솟값들을 저장
    for i in range(0, idx):
        if lm > a[i]:
            lm = a[i]
            answer.append(a[i])

    #가장 작은 풍선 이후에 끝에서부터 최솟값들을 저장
    for i in range(len(a)-1, idx, -1):
        if rm > a[i]:
            rm = a[i]
            answer.append(a[i])

    #만약에 배열에 가장 작은 풍선이 없다면 추가한다
    if m not in answer:
        answer.append(m)

    print(answer)
    return len(answer)

if __name__ == "__main__":
    print(solution(a = [3, 2, 5, -17, -18, 27, 65, -2, 58, -92, -71, -68, -61, -33, -85, 50]))