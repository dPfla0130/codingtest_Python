def solution(progresses, speeds):
    answer = []
    while progresses:
        idx = 0
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]

        while len(progresses)>0 and progresses[0]>=100:
            idx+=1
            progresses.pop(0)
            speeds.pop(0)
        if idx!=0:
            answer.append(idx)

    return answer

