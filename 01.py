import heapq

def sum_kth_largest(k):
    with open('01.in', 'r') as f:
        data = f.read()
        elf_calories = [-sum([int(y) for y in x.split("\n")]) for x in data.split("\n\n")]
        heapq.heapify(elf_calories)
        print(-sum([heapq.heappop(elf_calories) for _ in range(k)]))

def part1():
    sum_kth_largest(1)

def part2():
    sum_kth_largest(3)

part1()
part2()
