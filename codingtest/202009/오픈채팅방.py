def solution(record):
    answer = []
    arr = []
    user = {}
    for i in record:
        li = i.split()
        if li[0]=="Enter":
            user[li[1]] = li[2]
            arr.append((li[1], 1))
        elif li[0]=="Leave":
            arr.append((li[1], 0))
        else:
            user[li[1]] = li[2]
    for i in arr:
        if i[1]==1:
            answer.append(user.get(i[0])+ "님이 들어왔습니다.")
        else:
            answer.append(user.get(i[0]) + "님이 나갔습니다.")
    return answer

if __name__ == "__main__":
    print(solution(record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

