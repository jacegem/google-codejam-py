



def main():
    #inputFile = "A-small-attempt.in"
    inputFile = "B-small-attempt1.in"
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    testCase = int(inpf.readline())
    for case in range(testCase):
        #parties = int(inpf.readline())
        b, m = [int(x) for x in inpf.readline().strip().split(' ')]

        possible = "POSSIBLE"
        if b <= m: possible = "IMPOSSIBLE"

        result = 'Case #{}: {}\n'.format(case+1, possible)
        print result,
        outf.write(result)

        if possible == "POSSIBLE":
            first = True
            firstRow = []
            for r in range(b):
                row = ['0'] * b
                if first == True:
                    for i in range(m):
                        row[i] = '1'
                    first = False
                    firstRow = row
                elif r == b-1:
                    row[0] = '0'
                else:
                    if firstRow[b - 1 - r] == '1':
                        row[0] = '1'
                row = reversed(row)

                result = ''.join(row) + "\n"
                print result,
                outf.write(result)


        #rst = solve(b, m)


        #print n
        #print result,
        #outf.write(result)
    inpf.close()
    outf.close()

def main2():
    print str(unichr(65))
    return False


if __name__ == "__main__":
    main()
    #main2()

