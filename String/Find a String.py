def count_substring(string, sub_string):
    count1 = 0
    index = 0
    while string[index:].find(sub_string) != -1:
        count1 += 1
        index = index + string[index:].find(sub_string) + 1
    return count1


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)