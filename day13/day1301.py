def main(f):
    file1 = open(f, 'r')
    lines = file1.read().strip().splitlines()

    print(part1(lines))

#    part2(lines)

def part1(lines):  
    count = 0

    coord = []
    folddirection = ''
    foldvalue = 0
    count = 0
    for l in range(len(lines)):
        if len(lines[l]) > 0 and lines[l][0] != 'f':
            coord.append(list(map(int, lines[l].strip().split(','))))
        elif len(lines[l]) > 0 and lines[l][0] == 'f':
            foldlocation = lines[l].index('x')
            if foldlocation > 0:
                folddirection = lines[l][foldlocation]
                foldvalue = int(lines[l][foldlocation+2:len(lines[l])])
            break

    for c in range(len(coord)):
        if folddirection == 'y' and coord[c][1] > foldvalue:
            coord[c][1] = foldvalue - (coord[c][1] - foldvalue)
        if folddirection == 'x' and coord[c][0] > foldvalue:
            coord[c][0] = foldvalue - (coord[c][0] - foldvalue)
    
    for c1 in range(len(coord)):
        found = 0
        for c2 in range(c1 + 1, len(coord)):
            if coord[c2] == coord[c1]:
                found = 1
        if found == 0:
            count += 1

    return(count)

def part2(lines):
    count = 0

    return(count)

if __name__ == "__main__":
    main('input.txt')