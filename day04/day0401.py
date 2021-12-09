import math

def main(f):
    with open(f, "r") as file1:
        lines = [(line.strip()).split() for line in file1 if line.strip()]

    print(part1(lines))

    with open(f, "r") as file1:
        lines = [(line.strip()).split() for line in file1 if line.strip()]
    
    print(part2(lines))

def part1(lines):  # sourcery no-metrics
    winner = 0

    chosennumber = lines[0]
    chosen = chosennumber[0].split(",")

    horwinner = 0
    verwinner = 0
    horizontal = 0
    vertical = [0, 0, 0, 0, 0]
    lastnumber = 0
    startrow = 1

    for c in range(len(chosen)):
        for l in range(1, len(lines)):
            for r in range(len(lines[l])):
                if lines[l][r] == chosen[c]:
                    lines[l][r] = '-1'
                horizontal += int(lines[l][r])
                vertical[r] += int(lines[l][r])

            if l % 5 == 0:
                for item in vertical:
                    if item == -5:
                        verwinner = -5
                vertical = [0, 0, 0, 0, 0]   

            if horizontal == -5 or verwinner == -5:
                winner = 1
                winline = l
                lastnumber = int(chosen[c])
                break

            horizontal = 0

        if winner == 1:
            break
# count non chosen numbers on the board

    startrow = (
        winline - 4 if winline % 5 == 0 else (math.floor(winline / 5) * 5) + 1
    )

    for l in range(startrow, startrow + 5):
        for r in range(len(lines[l])):
            if lines[l][r] != '-1':
                horwinner += int(lines[l][r])

    return horwinner * lastnumber
    
def part2(lines):
    
    allwinlines = []
    numberofblocks = int((len(lines) - 1) / 5)
    numberofwinners = 0
    chosennumber = lines[0]
    chosen = chosennumber[0].split(",")
    horwinner = 0
    horizontal = 0
    vertical = [0, 0, 0, 0, 0]
    lastnumber = 0
    startrow = 1
    winline = 0

    for c in range(len(chosen)):
        for l in range(1, len(lines)):
            for r in range(len(lines[l])):
                if lines[l][r] == chosen[c]:
                    lines[l][r] = '-1'
                horizontal += int(lines[l][r])
                vertical[r] += int(lines[l][r])

            if l % 5 == 0:
                for item in vertical:
                    if item == -5 and l not in allwinlines:
                        numberofwinners += 1
                        winline = l
                        startrow = (winline - 4 if winline % 5 == 0 else (math.floor(winline / 5) * 5) + 1)
                        for i in range(startrow, startrow+5):
                            allwinlines.append(i)
                        lastnumber = int(chosen[c])
                vertical = [0, 0, 0, 0, 0]   

            if horizontal == -5 and l not in allwinlines:
                numberofwinners += 1
                winline = l
                startrow = (winline - 4 if winline % 5 == 0 else (math.floor(winline / 5) * 5) + 1)
                for i in range(startrow, startrow+5):
                    allwinlines.append(i)
                lines[l][0] = '-5'
                lines[l][1] = '-5'
                lines[l][2] = '-5'
                lines[l][3] = '-5'
                lines[l][4] = '-5'
                lastnumber = int(chosen[c])
                horizontal = 0

            horizontal = 0
        
        if numberofwinners == numberofblocks:
            break
# count non chosen numbers on the board
#    print(numberofwinners)
#    print(winline)
    startrow = (winline - 4 if winline % 5 == 0 else (math.floor(winline / 5) * 5) + 1)

    for l in range(startrow, startrow + 5):
        for r in range(len(lines[l])):
            if int(lines[l][r]) > 0:
                horwinner += int(lines[l][r])

    return horwinner * lastnumber

if __name__ == "__main__":
    main('input.txt')