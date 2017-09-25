from itertools import combinations

def encode_list(n, l):
    difference = 0
    for i in range(2, n+2):
        subset = combinations(l, i)
        for s in subset:
            difference += max(s) - min(s)
    return difference % (10**9 + 7)


def print_cases(func):
    for i in range(1, int(input())+1):
        n = int(input())
        l = list(map(int, input().split()))
        output = func(n, l)
        print("Case #{}: {}".format(i, output))

if __name__ == "__main__":
    print_cases(encode_list)

