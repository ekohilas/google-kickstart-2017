def num_cakes(area):
    cakes = tuple(x**2 for x in range(1, int(area ** 0.5) + 1))

    cache = {0: 0, 1: 1}
    def min_cakes(area):
        if area not in cache:
            cache[area] = min(
                min_cakes(area - cake)
                for cake in cakes
                if area - cake >= 0
            ) + 1

        return cache[area]

    #return min_cakes(area)

    def _get_change_making_matrix(set_of_coins, r):
        m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]

        for i in range(r + 1):
            m[0][i] = i

        return m

    def change_making(coins, n):
        m = _get_change_making_matrix(coins, n)

        for c in range(1, len(coins) + 1):

            for r in range(1, n + 1):

                if coins[c - 1] == r:
                    m[c][r] = 1

                elif coins[c - 1] > r:
                    m[c][r] = m[c - 1][r]

                else:
                    m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])

        return m[-1][-1]

    return change_making(cakes, area)


def print_cases(func):
    for i in range(1, int(input())+1):
        n = int(input())
        output = func(n)
        print("Case #{}: {}".format(i, output))

if __name__ == "__main__":
    print_cases(num_cakes)

'''
# Greedy solution
max_cake = math.floor(math.sqrt(area)) ** 2
while area:
    print(f"a: {area}, m: {max_cake} c: {cakes}")
    if area - max_cake >= 0:
        cakes += 1
        area -= max_cake
    else:
        max_cake = math.floor(math.sqrt(area)) ** 2
return cakes
'''
