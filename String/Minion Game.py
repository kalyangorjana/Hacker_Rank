def minion_game(string):
    kevin = 0
    l = len(string)
    for i in range(l):
        if string[i] in 'AEIOU':
            kevin += l - i

    stuart = int(l * (l + 1) / 2) - kevin

    if stuart > kevin:
        print('Stuart', stuart)
        return

    if kevin > stuart:
        print('Kevin', kevin)
        return

    print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
