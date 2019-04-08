def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = [False] * ((n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]


# if cipher_list[1] % second != 0:
#     first, second = second, first


def solve(prime_list, cipher_list):
    code_list = []

    c_number = cipher_list[0]

    for prime_idx in range(len(prime_list)):
        first = prime_list[prime_idx]

        if c_number % first == 0:
            second = c_number // first
            code_list.append(first)
            code_list.append(second)
            break

    is_first_right = True

    for cipher_idx in range(1, len(cipher_list)):
        c_number = cipher_list[cipher_idx]
        if c_number % second == 0:
            second = c_number // second
            code_list.append(second)
        else:
            is_first_right = False
            break

    if is_first_right is False:
        code_list = []
        c_number = cipher_list[0]

        for prime_idx in range(len(prime_list)):
            first = prime_list[prime_idx]

            if c_number % first == 0:
                second = c_number // first
                first, second = second, first
                code_list.append(first)
                code_list.append(second)
                break

        for cipher_idx in range(1, len(cipher_list)):
            c_number = cipher_list[cipher_idx]
            second = c_number // second
            code_list.append(second)

    sort_results = code_list.copy()
    sort_results = list(set(sort_results))
    sort_results.sort()
    sort_map = {}

    dec = 65

    for val in sort_results:
        sort_map[val] = chr(dec)
        dec += 1

    '''    
    print(sort_map)    
    JCJQ    
    {3: 'A', 5: 'B', 7: 'C', 11: 'D', 13: 'E', 17: 'F', 19: 'G', 23: 'H', 29: 'I', 31: 'J', 37: 'K', 41: 'L', 43: 'M', 47: 'N', 53: 'O', 59: 'P',
     61: 'Q', 67: 'R', 71: 'S', 73: 'T', 79: 'U', 83: 'V', 89: 'W', 97: 'X', 101: 'Y', 103: 'Z'}
    Case  # 1: CJQUIZKNOWBEVYOFDPFLUXALGORITHMS
    {2: 'A', 89: 'B', 109: 'C', 211: 'D', 239: 'E', 353: 'F', 479: 'G', 601: 'H', 701: 'I', 827: 'J', 883: 'K', 1021: 'L', 1051: 'M', 1087: 'N',
     1277: 'O', 1381: 'P', 1531: 'Q', 1571: 'R', 1669: 'S', 1861: 'T', 1973: 'U', 1997: 'V', 2137: 'W', 2213: 'X', 2281: 'Y', 2411: 'Z'}
    Case  # 2: SUBDERMATOGLYPHICFJKNQVWXZ    
    # '''

    result_list = list(map(lambda key: sort_map[key], code_list))
    return ''.join(result_list)


def main_submit():
    test_case = int(read_line())

    for case in range(1, test_case + 1):
        n, l = [int(s) for s in read_line().split(" ")]  # read a list of integers, 2 in this case
        cipher_list = [int(s) for s in read_line().split(" ")]

        prime_list = primes2(n)
        answer = solve(prime_list, cipher_list)

        result = 'Case #{}: {}'.format(case, answer)
        print(result)


def read_line():
    if isLocal is True:
        line = inp_file.readline()
    else:
        line = input()

    return line.strip()


isLocal = True
inp_file = ''

if __name__ == "__main__":
    if isLocal is True:
        inp_file = open('input_file.txt', "r")

    main_submit()
