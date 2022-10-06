n = int(input())
final_list = []
input_list = []
while n > 0:
    user_choice = input()
    user_list = user_choice.split()
    if user_list[0] == 'insert':
        input_list.insert(int(user_list[1]), int(user_list[2]))
    elif user_list[0] == 'append':
        input_list.append(int(user_list[1]))
    elif user_list[0] == 'remove':
        input_list.remove(int(user_list[1]))
    elif user_list[0] == 'sort':
        input_list.sort()
    elif user_list[0] == 'pop':
        input_list.pop()
    elif user_list[0] == 'reverse':
        input_list.reverse()
    else:
        final_list.append(list(input_list))
    n -= 1
for i in final_list:
    print(i)
