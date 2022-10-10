def solve(s):
    print(" ".join([i.capitalize() for i in s.split(" ")]))


if __name__ == '__main__':
    s = input()
    solve(s)