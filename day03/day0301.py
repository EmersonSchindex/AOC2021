def main(f):
    file1 = open(f, 'r')
    lines = file1.read().splitlines()
    print(part1(lines))
    print(part2(lines))

def part1(lines):    # sourcery skip: inline-variable, square-identity, use-join
    count0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    gamma = ''
    epsilon = ''
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '0':
                count0[j] += 1
            else:
                count1[j] += 1

    for i in range(len(lines[0])):
        if int(count0[i]) > int(count1[i]):
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'             
    
    return int(gamma, 2) * int(epsilon, 2)
    
def part2(lines):  # sourcery no-metrics skip: assign-if-exp
    winner = ''
    oxygen = ''
    scrubber = ''
    oxyint = 0
    newlines = []
    savelines = lines.copy()
    j = 0

# determine oxygen

    while len(newlines) != 1:
        if j == 0:
            copyline = [int(lines[i][j]) for i in range(len(lines))]
        else:
            copyline = [int(newlines[i][j]) for i in range(len(newlines))]

        if sum(copyline) >= len(copyline) / 2:
            oxygen += '1'
            winner = '1'
        else:
            oxygen += '0'
            winner = '0'
    
        copyline.clear()
        
        if j > 0:
            lines = newlines.copy()
            newlines.clear()
        
        for i in range(len(lines)):
            if lines[i][j] == winner:
                newlines.append(lines[i])
   
        j += 1

    oxyint = int(newlines[0], 2)

# determine scrubber

    newlines = []
    lines = savelines.copy()
    j = 0
    
    while len(newlines) != 1:
        if j == 0:
            copyline = [int(lines[i][j]) for i in range(len(lines))]
        else:
            copyline = [int(newlines[i][j]) for i in range(len(newlines))]

        if sum(copyline) >= len(copyline) / 2:
            scrubber += '0'
            winner = '0'
        else:
            scrubber += '1'
            winner = '1'
    
        copyline.clear()
        
        if j > 0:
            lines = newlines.copy()
            newlines.clear()
        
        for i in range(len(lines)):
            if lines[i][j] == winner:
                newlines.append(lines[i])
   
        j += 1

    return oxyint * int(newlines[0], 2)

if __name__ == "__main__":
    main('input.txt')