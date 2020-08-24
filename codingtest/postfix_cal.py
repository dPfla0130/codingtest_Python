import sys
sys.stdin = open("in2.txt", "r")
a = input()

stack = []
for i in a:
    if i.isdecimal():
        stack.append(int(i))
    elif i.isdecimal()!=True:
        a = stack.pop()
        b = stack.pop()
        if i=="+":
            res = b + a
        elif i=="-":
            res = b - a
        elif i=="*":
            res = b * a
        elif i=="/":
            res = b / a
        stack.append(res)
        
for i in stack:
    print(i)
