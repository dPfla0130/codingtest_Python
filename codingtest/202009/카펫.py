def solution(brown, red):
    answer = []
    carpetsize = brown + red
    for i in range(3, carpetsize//2+1):
        if carpetsize % i == 0 and i >= carpetsize//i:
            #print(i, carpetsize//i)
            if red == ((i-2) * ((carpetsize//i)-2)):
                answer = [i, carpetsize//i]
    return answer

if __name__ == "__main__":
    print(solution(brown=8, red=1))