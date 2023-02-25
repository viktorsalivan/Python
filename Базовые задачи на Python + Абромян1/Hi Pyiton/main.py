s = str(input("Ввидите скобку:\n"))


def check(s):
    res = 0
    for skobka in s:
        if skobka == "(":
            res += 1
        else:
            res -= 1
        if res < 0:
            return False
    if not(res):
        return True
    else:
        return False


temp = check(s)
print(temp)
