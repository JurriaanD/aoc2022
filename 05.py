import re

def part1():
    with open('05.in') as f:
        num_stacks = len(f.readline()) // 4
        stacks = [[] for _ in range(num_stacks)]
        f.seek(0)

        while (line := f.readline().rstrip('\n')):
            if line[1] == '1':
                f.readline()
                break

            for i in range(num_stacks):
                c = line[1 + 4*i]
                if (c != ' '):
                    stacks[i].insert(0, c)

        while (line := f.readline().rstrip('\n')):
            num, source, to = map(int,re.findall('\d+', line))
            for _ in range(num):
                stacks[to-1].append(stacks[source-1].pop())

        print(''.join([s[-1] for s in stacks]))

def part2():
    with open('05.in') as f:
        num_stacks = len(f.readline()) // 4
        stacks = [[] for _ in range(num_stacks)]
        f.seek(0)

        while (line := f.readline().rstrip('\n')):
            if line[1] == '1':
                f.readline()
                break

            for i in range(num_stacks):
                c = line[1 + 4*i]
                if (c != ' '):
                    stacks[i].insert(0, c)

        while (line := f.readline().rstrip('\n')):
            num, source, to = map(int,re.findall('\d+', line))
            stacks[to-1].extend(stacks[source-1][-num:])
            del stacks[source-1][-num:]

        print(''.join([s[-1] for s in stacks]))

part1()
part2()
