def main(s:str) -> None:
    length = len(s)
    res = 0
    flag = False

    for i in range(1,length//2):
        if s[i] != s[i-1]:
            flag = True

    if flag:
        res = 2
        while len(s) % 2 == 0:
            if s[:len(s)//2] != s[len(s)//2:]:
                res = 1
                break
            s = s[:len(s)//2]

    if res:
        print(res)
    else:
        print("Impossible")
