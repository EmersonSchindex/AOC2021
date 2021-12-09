def main(f):
    with open(f, "r") as file1:
        lines = [(line.strip()).split('|') for line in file1 if line.strip()]

#    print(part1(lines))
    print(part2(lines))

def part1(lines):  # sourcery no-metrics

    numberofcodes = 0
    
    for l in range(len(lines)):
        teststring = lines[l]
        teststring[1].split(',')
        for code in teststring[1].split(" "):
            if len(code) in(2, 3, 4, 7):
                numberofcodes += 1

    return numberofcodes
    
def part2(lines):

    numberofcodes = 0
    
    for l in range(len(lines)):
        teststring = lines[l]
        teststring[1].split(',')
        for code in teststring[1].split(" "):
            if len(code) in(2, 3, 4, 7):
                numberofcodes += 1

    return numberofcodes
    
if __name__ == "__main__":
    main('test.txt')