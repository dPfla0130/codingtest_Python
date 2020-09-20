def solution(monster, S1, S2, S3):
    cnt = 0

    for i in range(1, S1+1):
        for j in range(1, S2+1):
            for k in range(1, S3+1):
                if i+j+k+1 in monster:
                    cnt += 1

    answer = int((((S1 * S2 * S3) - cnt) / (S1 * S2 * S3)) * 1000)
    return answer

if __name__ == "__main__":
    print(solution(monster=[4,9,5,8], S1=2, S2=3, S3=3))