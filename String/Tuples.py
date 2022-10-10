if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuple_1 = ()
    for i in integer_list:
        tuple_1 += (i,)
    print(hash(tuple_1))
