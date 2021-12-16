from copy import deepcopy

def main(f):
    file1 = open(f, 'r')
    lines = file1.read().strip().splitlines()

    print(part1(lines))

def insertletters(start, copystart, single, pairs):
    x = 0
    for s in range(len(start) - 1):
        testlet = pairs.index(start[s] + start[s+1])
        copystart.insert(s+1+x, single[pairs.index(start[s] + start[s+1])])
        x += 1

    return(copystart)

def part1(lines):
    poltemp = []
    copytemp = []
    for l in range(len(lines[0])):
        poltemp.append(lines[0][l])
        copytemp.append(lines[0][l])

    pairs = []
    single = []
    for l in range(2, len(lines)):
        pairs.append(str(lines[l])[:2])
        single.append(str(lines[l])[-1])  

    for c in range(10):
        polresult = insertletters(poltemp, copytemp, single, pairs)
        poltemp = deepcopy(polresult)
    
    telB, telC, telS, telF, telN, telP, telH, telO, telV, telK = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for p in range(len(polresult)):
        if polresult[p] == 'B':
            telB += 1
        if polresult[p] == 'C':
            telC += 1
        if polresult[p] == 'H':
            telH += 1
        if polresult[p] == 'N':
            telN += 1
        if polresult[p] == 'S':
            telS += 1
        if polresult[p] == 'F':
            telF += 1
        if polresult[p] == 'P':
            telP += 1
        if polresult[p] == 'O':
            telO += 1
        if polresult[p] == 'V':
            telV += 1
        if polresult[p] == 'K':
            telK += 1
    
    tellist = [telB, telC, telH, telN, telS, telF, telP, telO, telV, telK]
    maxtel = max(tellist)
    mintel = min(tellist)
    
    return(maxtel - mintel)

if __name__ == "__main__":
    main('input.txt')