def print_cases(func):
    for i in range(1, int(input())+1):
        line = input()
        output = func()
        print("Case #{}: {}".format(i, output))

if __name__ == "__main__":
    #print_cases()

