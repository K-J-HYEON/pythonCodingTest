def solve(num: str) -> str:
    while True:
        tmp = str(sum([int(x) for x in num])) # 주어진 숫자의 각 자릿수를 더한다.
        if len(tmp) == 1:
            break
        else:
            num = tmp
    return tmp

if __name__ == '__main__':
    while True:
        num = input()
        if num == '0':
            break
        print(solve(num))