def solution(max_weight, specs, names):
    answer = 0
    specs = dict(specs)
    weight = 0
    for name in names:
        if weight + int(specs[name]) > max_weight:
            answer += 1
            weight = 0
        weight += int(specs[name])

    return answer + 1

if __name__ == "__main__":
    print(solution(max_weight=200, specs=[["toy",200], ["snack", 70]], names=["toy", "snack", "toy", "snack"]))

