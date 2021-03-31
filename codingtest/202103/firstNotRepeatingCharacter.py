def firstNotRepeatingCharacter(s):
    repeat = dict()
    for i in s:
        try:
            repeat[i] += 1
        except:
            repeat[i] = 1
    for k, v in repeat.items():
        if v == 1:
            return k
    return '_'


if __name__ == "__main__":
    print(firstNotRepeatingCharacter("abacabad"))