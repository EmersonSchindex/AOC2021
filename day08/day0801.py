def main(f):
    with open(f, "r") as file1:
        lines = [(line.strip()).split('|') for line in file1 if line.strip()]

    print(lines)
#    print(part1(lines))
#   print(part2(lanternfish))

def part1(lines):  # sourcery no-metrics

    numberofchars = 0

    for l in range(1, len(lines), 2):
        for ll in range(len(lines[l])):

            print(lines[l], end =" ")

    return numberofchars
    
def part2(fish):

    y = 2
    
    return y

if __name__ == "__main__":
    main('test.txt')