from math import ceil

def part1():
    with open("10.in") as f:
        cycle = 1
        register = 1
        signal_strength = 0

        for line in [x.rstrip() for x in f.readlines()]:
            start_cycle = cycle
            start_cycle_next_op = None
            start_value = register
            end_value = register

            next_important = 20 if cycle <= 20 else ceil(((cycle - 20) / 40)) * 40 + 20

            tokens = line.split()
            if tokens[0] == "noop":
                start_cycle_next_op = start_cycle + 1
                end_value = start_value

            elif tokens[0] == "addx":
                start_cycle_next_op = start_cycle + 2
                end_value = start_value + int(tokens[1])

            register = end_value
            cycle = start_cycle_next_op

            if start_cycle <= next_important < start_cycle_next_op:
                signal_strength += next_important * start_value
                print(f"Register value @{next_important}: {start_value}")

        print("Signal strength: ", signal_strength)


def part2():
    with open("10.in") as f:
        register = 1

        ops = []
        for line in [x.rstrip() for x in f.readlines()]:
            tokens = line.split()
            if tokens[0] == "noop":
                ops.append([1, "noop"])
            else:
                ops.append([2, ["addx", int(tokens[1])]])

        for row in range(0, 6):
            for col in range(0, 40):
                if (register - 1 <= col <= register + 1):
                    print('#', end='')
                else:
                    print('.', end='')

                remaining_cycles, op = ops[0]

                if remaining_cycles == 1:
                    if op == "noop":
                        pass
                    else:
                        register += op[1]
                    del ops[0]
                else:
                    ops[0][0] -= 1
            print()


part1()
part2()
