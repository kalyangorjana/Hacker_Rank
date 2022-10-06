def split_and_join(line):
    # final_str = ""
    # a = line.split(" ")
    # for i in a:
    #     final_str += i
    #     if a.index(i) != len(a)-1:
    #         final_str += "_"
    # return final_str

    return line.replace(" ", "-")


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)