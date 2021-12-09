def main(f):
    file1 = open(f, 'r')
    lines = file1.read().splitlines()
    part1(lines)
    part2(lines)

def part1(lines):  
    count = 0
    firstline = 0
    depth = 0
    for line in lines:
        if firstline == 0:
            firstline = 1
        elif int(line) > depth:
            count += 1
        depth = int(line)
    print(count)

def part2(lines):
    count = 0
    loopcount = 0
    depth = 0
    start = int(lines[0]) + int(lines[1]) + int(lines[2])
    for i in range(1, len(lines)):
        depth += int(lines[i])
        loopcount += 1
        if loopcount == 3:
            if depth > start:
                count += 1
            start = depth
            depth -= int(lines[i - 2])
            loopcount = 2

    print(count)

if __name__ == "__main__":
    main('input.txt')