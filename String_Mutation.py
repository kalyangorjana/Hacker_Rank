def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    final_string = "".join(string)
    return str(final_string)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)