def print_rangoli(size):
    alphabet = ' abcdefghijklmnopqrstuvwxyz'

    for i in range(size, 0, -1):
        c = alphabet[size:i:-1] + alphabet[i:size + 1]
        c = '-'.join(c)
        print(c.center((size * 4) - 3, '-'))

    for i in range(0, size - 1):
        c = alphabet[size:i + 2:-1] + alphabet[i + 2:size + 1]
        c = '-'.join(c)
        print(c.center((size * 4) - 3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

    # MY CODE
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # alphabet_size = (size * 4) - 3
    # final_string = alphabet[size - 1:0:-1] + alphabet[:size]
    # j = 0
    # for i in range(1, (size * 2)):
    #     if i < size:
    #         print("-".join(final_string[size - i:size + j]).center(alphabet_size, '-'))
    #         j += 1
    #     if i == size:
    #         print("-".join(final_string).center(alphabet_size, '-'))
    #
    #     if i > size:
    #         j -= 1
    #         print("-".join(final_string[i - size:size+j]).center(alphabet_size, '-'))


