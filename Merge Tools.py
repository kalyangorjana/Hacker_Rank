def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(i)
        result = ""
        for j in range(k):
            if string[i + j] not in result:
                result += string[i + j]
        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# my code Before refine
# def merge_the_tools(string, k):
#     s_list = []
#     s_list1 = []
#     s = ""
#     for i in range(0, len(string), k):
#         s_list.append(string[i:i+k])
#     for i in s_list:
#         s = ""
#         for j in i:
#             if j in s:
#                 pass
#             else:
#                 s = s + j
#         s_list1.append(s)
#     for i in s_list1:
#         print(i)
#
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)
