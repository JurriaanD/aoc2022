def part1():
    with open ('03.in') as f:
        backpacks = f.read().split('\n')
        score = 0
        for backpack in backpacks:
            middle = len(backpack) // 2
            common = [x for x in backpack[:middle] if x in backpack[middle:]][0]
            score += ord(common) - [97, 39][common.isupper()] + 1
        print(score)

def part2():
    with open ('03.in') as f:
        backpacks = f.read().split('\n')
        score = 0
        for i in range(0, len(backpacks), 3):
            common = "".join({x for x in backpacks[i] if x in backpacks[i+1] and x in backpacks[i+2]})
            score += ord(common) - [97, 39][common.isupper()] + 1
        print(score)

part1()
part2()