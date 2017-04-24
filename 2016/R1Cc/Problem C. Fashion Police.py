



def overK(jj, pp, ss, k, rst):
    same = 0
    jp = 0
    js = 0
    ps = 0
    for r in rst:
        j, p, s = [int(x) for x in r.split(' ')]

        if jj == j and pp == p:
            jp += 1
        if jj == j and ss == s:
            js += 1
        if pp == p and ss == s:
            ps += 1
        if jp > k or js > k or ps > k:
            return True
    return False

def getRange(j):
    return range(1, j+1)

def solve(j,p,s,k):
    rst = []
    for jj in getRange(j):
        for pp in getRange(p):
            for ss in getRange(s):
                if overK(jj, pp, ss, k, rst):
                    continue
                else:
                    rst.append(str(jj) + ' ' +str(pp) + ' '+ str(ss))
    return rst


def main():
    #inputFile = "A-small-attempt.in"
    inputFile = "sample.in"
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    testCase = int(inpf.readline())
    for case in range(testCase):

        j, p, s, k = [int(x) for x in inpf.readline().strip().split(' ')]
        print j, p, s, k
        rst = solve(j,p,s,k)
        result = 'Case #{}: {}\n'.format(case+1,  len(rst))
        print result,
        outf.write(result)
        result = '\n'.join(rst) + "\n"
        #print n
        print result,
        outf.write(result)
    inpf.close()
    outf.close()

def main2():
    print str(unichr(65))
    return False


if __name__ == "__main__":
    main()
    #main2()

