def calc(n):
    a, b, c = 0, 0, 1

    if n == 0:
        return a

    for i in range(n):
        a, b, c = b, c, a+b+c

    return a

if __name__ == '__main__':
    n = int(input('番号を指定してください（0以上の整数）: '))

    answer = calc(n)
    print('トリボナッチ数列の{}番目の値は{}です'.format(n, answer))