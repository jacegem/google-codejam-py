# Problem C
import math


def get_min_speed(max_speed, d, ki, si):
    kps = (d - ki)/si
    speed = d / kps
    return min(max_speed, speed)


def main():
    # inputFile = 'A-small-attempt2.in'
    inputFile = 'A-large.in'
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    test_case = int(inpf.readline())

    for case in range(test_case):

        d, n = [int(x) for x in inpf.readline().strip().split(' ')]

        min_speed = math.inf

        for i in range(n):
            ki, si = [int(x) for x in inpf.readline().strip().split(' ')]
            min_speed = get_min_speed(min_speed, d, ki, si)

        result = 'Case #{}: {:.6f}\n'.format(case + 1, min_speed)
        print(result, end='')
        outf.write(result)

    inpf.close()
    outf.close()





if __name__ == "__main__":
    main()
    #ma, mi = solve(999999, 262144)