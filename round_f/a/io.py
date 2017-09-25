def worst_case(n, l):
    s_l = sorted(l)

    mid = l.pop((n-1)//2)
    while l:
        if mid == s_l[0]:
            s_l.pop(0)
        elif mid == s_l[-1]:
            s_l.pop()
        else:
            return "NO"
        mid = l.pop((len(l)-1)//2)

    return "YES"


def print_cases(func):
    for i in range(1, int(input())+1):
        n = int(input())
        l = list(map(int, input().split()))
        output = func(n, l)
        print("Case #{}: {}".format(i, output))

if __name__ == "__main__":
    print_cases(worst_case)

