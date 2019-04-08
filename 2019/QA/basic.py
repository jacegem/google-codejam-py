# QA




CHARGE = 'C'
SHOOT = 'S'
IMPOSIBBLE = 'IMPOSSIBLE'


def get_min_damage(program):
    shoot_count = 0

    for x in program:
        if x is SHOOT:
            shoot_count += 1

    return shoot_count


def get_damage(program):
    total_damage = 0
    charge = 1

    for x in program:
        if x is CHARGE:
            charge *= 2
        elif x is SHOOT:
            total_damage += charge

    return total_damage


def hack(program):
    """
    find last index of change from `C` to `S`
    :param program: 
    :return: 
    """
    # 'CSSSC'
    last_state = ''
    last_idx = 0

    for idx in range(len(program)):
        state = program[idx]
        if last_state is CHARGE and state is SHOOT:
            last_idx = idx
            last_state = state
        else:
            last_state = state

    if last_idx is 0:
        return program

    program_list = list(program)
    program_list[last_idx - 1] = SHOOT
    program_list[last_idx] = CHARGE
    program = "".join(program_list)

    return program


def solve(max_damage, program):
    damage = get_damage(program)

    if max_damage >= damage:
        return "0"

    min_damage = get_min_damage(program)

    if min_damage > max_damage:
        return IMPOSIBBLE

    hacked = program
    hack_count = 1

    while True:
        hacked = hack(hacked)
        damage = get_damage(hacked)
        if damage <= max_damage:
            return hack_count
        else:
            hack_count += 1


def main():
    inputFile = 'A-small.in'
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    test_case = int(inpf.readline())

    for case in range(test_case):
        max_damage, program = inpf.readline().strip().split(' ')
        max_damage = int(max_damage)
        answer = solve(max_damage, program)

        result = 'Case #{}: {}\n'.format(case + 1, answer)
        print(result, end='')
        outf.write(result)

    inpf.close()
    outf.close()


def main_submit():
    test_case = int(input())  # read a line with a single integer

    for case in range(1, test_case + 1):
        max_damage, program = input().split(" ")
        max_damage = int(max_damage)
        answer = solve(max_damage, program)
        result = 'Case #{}: {}'.format(case, answer)
        print(result)

if __name__ == "__main__":
    main_submit()

