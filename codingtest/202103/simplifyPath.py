def simplifyPath(path):
    simple = ''
    directory = path.split("/")
    i = 0
    print(directory)
    while 0 <= i < len(directory):
        if directory[i] == '' or directory[i] == '.':
            directory.pop(i)
            i -= 1
        elif directory[i] == '..':
            print(i)
            if i-1 >= 0:
                directory.pop(i)
                i -= 1
                directory.pop(i)
                i -= 1

            elif i == 0:
                directory.pop(0)
                i -= 1
            print(directory)
        i += 1
    if not directory:
        return '/'

    simple = simple.join('/'+j for j in directory)
    if len(directory)>1 and simple[-1] == '/':
        return simple[:-1]
    return simple


if __name__ == "__main__":
    print(simplifyPath("/.././///"))