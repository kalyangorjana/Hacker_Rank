def print_formatted(number):
    for i in range(1, number+1):
        width = len(bin(number)[2:])
        print(f"{str(i).rjust(width)} {str((oct(i))[2:]).rjust(width)} {(str(hex(i).upper())[2:]).rjust(width)} {(str(bin(i))[2:]).rjust(width)}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
