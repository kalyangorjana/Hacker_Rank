# Optimistic Way
s = input()
n = int(s[:(s.find(' '))])
m = n * 3
num = 1
for i in range(n):
    if i < int(n / 2):
        print(('.|.'*num).center(m, '-'))
        num += 2
    if i == int(n / 2):
        print('WELCOME'.center(m, '-'))
    if i > int(n / 2):
        print(('.|.'*num).center(m, '-'))
        num -= 2


# #My Logic
# thickness = input().split()
# row = int(thickness[0])
# column = int(thickness[1])
# # c = '-'
# d = '.|.'
# e = 'WELCOME'
# c_count = 1
# column = int((column1-3)/2)
# for i in range(1, row+1):
#     if i < (int(((row-1)/2)+1)):
#         print((c*column) + (d*c_count) + (c*column))
#         column -= 3
#         c_count += 2
#     if i == (int(((row-1)/2)+1)):
#         print(e.center(column1, '-'))
#     if i > (int(((row-1)/2)+1)):
#         column += 3
#         c_count -= 2
#         print((c*column) + (d*c_count) + (c*column))
