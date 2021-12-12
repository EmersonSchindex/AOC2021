def main(f):
    with open(f, "r") as file1:
        lines = [(line.strip()).split('|') for line in file1 if line.strip()]

    print(part1(lines))

def part1(lines):

    graph = {}
    
    for l in range(len(lines)):
        teststring = str(lines[l])
        sleutel = teststring[2 : int(teststring.index('-'))]
        waarde = teststring[int(teststring.index('-')) + 1 : len(teststring) - 2]
        graph.setdefault(sleutel, list()).append(waarde)
        graph.setdefault(waarde, list()).append(sleutel)

    return graph

def part2(lines):
    finalscore = 0

    return finalscore

if __name__ == "__main__":
    main('test.txt')