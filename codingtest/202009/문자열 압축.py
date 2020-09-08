def countnum(i, s, answer):
    #문자열을 i 길이만큼 잘라 비교한다
    cnt = 0
    #처음 시작 문자열
    bmp = s[0:i]
    idx = -i
    length = 0
    while idx<len(s):
        idx += i
        cmp = s[idx:idx+i]
        #만약 전 문자열과 현재 자른 문자열이 같다면
        if bmp == cmp:
            #압축 갯수 1늘리기
            cnt += 1
        else:
            if cnt>1:
                length += len(str(cnt))+len(bmp)
                #만약에 현재 압축한 문자열 길이가 최소 길이값보다 작을 때
                #Max 값 반환
                if length >= answer:
                    return 9999
            else:
                length += len(bmp)
            cnt = 0
            bmp = cmp
            idx -= i
    return length

def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        res = countnum(i, s, answer)
        if res < answer:
            answer = res
    return answer

if __name__=="__main__":
    print(solution(s="aabbaccc"))
    print(solution(s="ababcdcdababcdcd"))
    print(solution(s="abcabcdede"))
    print(solution(s="abcabcabcabcdededededede"))
    print(solution(s="xababcdcdababcdcd"))

