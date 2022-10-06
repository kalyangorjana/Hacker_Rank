def swap_case(s):
    swap_str = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                swap_str += i.capitalize()
            else:
                swap_str += i.lower()
        else:
            swap_str += i
    return swap_str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
