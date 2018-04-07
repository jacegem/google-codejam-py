import math


class Pancake:
    def __init__(self, r, h):
        self.r = r
        self.h = h
        self.surface = 2 * math.pi * r * h
        self.top = math.pi * r * r
        self.top_surface = self.top + self.surface

    def get_top_surace(self):
        return self.top_surface

    def sort_surface(self):
        return self.surface


def get_max_top(k, pancakes):
    pancakes.sort(key=lambda x: x.top, reverse=True)

    pancake = pancakes[0]
    result = pancake.top + pancake.surface

    if k is 1:
        return result

    for i in range(k - 1):
        result += pancakes[i].surface

    return result


def get_max3(k, pancakes):
    max_top = get_max_top(k, pancakes)
    max_surface = get_max_surface(k, pancakes)


def get_max_surface(k, pancakes):
    max_top_surface = 0
    max_pancake = None
    for pancake in pancakes:
        if max_pancake is None:
            max_pancake = pancake
        top_surface = pancake.get_top_surace()
        if top_surface > max_top_surface:
            max_top_surface = top_surface
            max_pancake = pancake
    result = max_top_surface
    pancakes.remove(max_pancake)

    if k is 1:
        return result

    pancakes.sort(key=lambda x: x.surface, reverse=True)

    pancake_len = len(pancakes)

    for i in range(pancake_len):
        pancake = pancakes[i]

    for i in range(k-1):
        result += pancakes[i].surface

    return result


def get_max(k, pancakes):
    max_result = 0
    pancakes.sort(key=lambda x: x.r, reverse=True)
    for i in range(len(pancakes)):
        base = pancakes[i]
        result = base.top + base.surface

        pancake_height = []
        for pancake in pancakes:
            if pancake is base:
                continue
            if base.r >= pancake.r:
                pancake_height.append(pancake)

        if len(pancake_height) >= k-1:
            pancake_height.sort(key=lambda x: x.h, reverse=True)
            for j in range(k-1):
                result += pancake_height[j].surface
        else:
            result = 0

        if result > max_result:
            max_result = result

    return max_result


def main():
    inputFile = 'A-small-attempt3.in'
    # inputFile = 'A-large.in'
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    test_case = int(inpf.readline())

    for case in range(test_case):

        n, k = [int(x) for x in inpf.readline().strip().split(' ')]
        pancakes = []
        for i in range(n):
            r, h = [int(x) for x in inpf.readline().strip().split(' ')]

            pancake = Pancake(r, h)
            pancakes.append(pancake)

        result = get_max(k, pancakes)
        result = 'Case #{}: {:.9f}\n'.format(case + 1, result)
        print(result, end='')
        outf.write(result)

    inpf.close()
    outf.close()


if __name__ == "__main__":
    main()


