# Complete the solution so that it reverses the string passed into it.

def solution(string):
    y = -1
    x = ""
    for i in range(len(string)):
        x = x + string[y]
        y = y - 1
    print(x)


solution("Hello, World")
