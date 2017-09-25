import networkx as nx
from pprint import pprint

def expected_time(nodes, edges, p, g):
    G = nx.Graph()
    G.add_weighted_edges_from(g)

    lengths = nx.floyd_warshall(G)
    node_sum = {
            node: sum(d.values())
            for node, d in lengths.items()
    }

    cache = {}
    def recurse(last, depth):

        if (last, depth) not in cache:
            if depth == 1:
                cache[(last, depth)] = node_sum[last]
            else:
                cache[(last, depth)] = sum(
                    recurse(n, depth - 1)
                    for n in range(1, nodes + 1)
                    if n != last
                ) + node_sum[last]
            cache[(last, depth)] /= (nodes - 1)
        return cache[(last, depth)]

    #pprint(cache)
    return recurse(1, p)

def print_cases(func):
    for i in range(1, int(input())+1):
        n, m, p = map(int, input().split())
        g = [
                tuple(map(int, input().split()))
                for _ in range(m)
            ]
        output = func(n, m, p, g)
        print("Case #{}: {}".format(i, output))

if __name__ == "__main__":
    print_cases(expected_time)
    '''
    sums = {}
    for k in lengths:
        for n in range(1, nodes+1):
            if n != k:
                if n not in sums:
                    sums[n] = 0
                sums[n] += sum(lengths[k].values())
    '''

'''

    def recurse(last, total, depth):

        if depth > 0:

            total *= nodes - 1
            total += sums[last]

            for n in range(1, nodes+1):
                if n != last:
                    print(f"d: {depth}, t:{total}, n:{n}")
                    total += recurse(n, total, depth - 1)

            return total

        else:
            return 0

    cache = {}
    def recurse(last, prev, depth):

        if (last, depth) not in cache:
            if depth:
                cache[(last, depth)] = sum(
                    recurse(n, prev, depth - 1)
                    for n in range(1, nodes + 1)
                    if n != last
                )
            else:
                cache[(last, depth)] = prev
        return cache[(last, depth)]


    total = sum(lengths[1].values())
    total = recurse(1, total, p - 1)
    pprint(cache)
'''
