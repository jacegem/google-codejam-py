import math


class Schedule():
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end




def get_count(schedules):
    schedules.sort(key=lambda x: x.start)

    start_time = schedules[0].start
    end_time = 1440 - schedules[-1].end
    change_time = 0
    c_time
    j_time

    name = 'x'
    for schedule in schedules:
        if schedule.name is not name:




def main():
    inputFile = 'A-small-attempt3.in'
    # inputFile = 'A-large.in'
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    test_case = int(inpf.readline())

    for case in range(test_case):

        c, j = [int(x) for x in inpf.readline().strip().split(' ')]

        schedules = []
        for i in range(c):
            start, end = [int(x) for x in inpf.readline().strip().split(' ')]
            schedules.append(Schedule('c', start, end))
        for i in range(j):
            start, end = [int(x) for x in inpf.readline().strip().split(' ')]
            schedules.append(Schedule('j', start, end))

        result = get_count(schedules)

        result = 'Case #{}: {}\n'.format(case + 1, result)
        print(result, end='')
        outf.write(result)

    inpf.close()
    outf.close()


if __name__ == "__main__":
    main()


