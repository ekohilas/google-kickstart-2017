def max_honor(e, n, s):
    h = 0
    s.sort()
    while s:
        # dance
        if e > s[0]:
            e -= s.pop(0)
            h += 1
        else:
            # recruit
            if len(s) > 1 and s[-1] >= s[0] and h > 0:
                e += s.pop()
                h -= 1
            else:
                break
    return h

def print_cases(func):
    for i in range(1, int(input())+1):
        e, n = map(int, input().split())
        s = list(map(int, input().split()))
        output = func(e, n, s)
        print("Case #{}: {}".format(i, output))

if __name__ == "__main__":
    print_cases(max_honor)
