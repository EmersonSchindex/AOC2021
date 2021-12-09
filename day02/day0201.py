def main(f):
    file1 = open(f, 'r')
    lines = file1.read().splitlines()
    print(part1(lines))
    print(part2(lines))

def part1(lines):    # sourcery skip: inline-variable, square-identity
    horpos = verpos = 0
    for i in range(len(lines)):
        if lines[i][0] == 'f':
            horpos += int(lines[i][len(lines[i])-1])
        elif lines[i][0] == 'd':
            verpos += int(lines[i][len(lines[i])-1])
        else:
            verpos -= int(lines[i][len(lines[i])-1])
    
    return horpos * verpos

def part2(lines):
    horpos = depth = aim = 0
    for i in range(len(lines)):
        if lines[i][0] == 'f':
            horpos += int(lines[i][len(lines[i])-1])
            depth += (int(lines[i][len(lines[i])-1]) * aim)
        elif lines[i][0] == 'd':
            aim += int(lines[i][len(lines[i])-1])
        else:
            aim -= int(lines[i][len(lines[i])-1])
    
    return horpos * depth

if __name__ == "__main__":
    main('input.txt')