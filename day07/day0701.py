def main(f):
    with open(f, "r") as file1:
        crab = [(line.strip()).split(',') for line in file1 if line.strip()]

    crabpos = [int(crab[0][l]) for l in range(len(crab[0]))]

    print(part1(crabpos))
    print(part2(crabpos))

def part1(crab):  # sourcery no-metrics
    position = 0
    fuel = 0
    finalfuel = 0

    for i in range(len(crab)):
        position = crab[i]
        fuel = sum(abs(position - crab[c]) for c in range(len(crab)))
        if i != 0 and fuel < finalfuel or i == 0:
            finalfuel = fuel

    return finalfuel
    
def part2(crab):
    position = 0
    maxposition = max(crab)
    fuel = 0
    finalfuel = 0
    steps = 0

    for i in range(maxposition):
        position = i
        fuel = 0
        for c in range(len(crab)):
            steps = abs(position - crab[c])
            for n in range(steps + 1):
                fuel += n
        if position != 0 and fuel < finalfuel or position == 0:
            finalfuel = fuel

    return finalfuel

if __name__ == "__main__":
    main('input.txt')