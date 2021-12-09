def main(f):
    with open(f, "r") as file1:
        lines = [(line.strip()).split(',') for line in file1 if line.strip()]

    lanternfish = [int(lines[0][l]) for l in range(len(lines[0]))]
#    print(part1(lanternfish))
    print(part2(lanternfish))

def part1(fish):  # sourcery no-metrics

    for _ in range(1, 81):

        for f in range(len(fish)):
            if fish[f] == 0:
               fish.append(8)
               fish[f] = 6         
            else:
                fish[f] = fish[f] - 1

    return len(fish)
    
def part2(fish):

    fishperday = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    fishdaycount = 0
    fishday6and8 = 0
    totalfish = 0

    for f in range(len(fish)):
        fishperday[fish[f]] += 1

    for d in range(1, 257):
        for f in range(len(fishperday)):
            fishdaycount = fishperday[f]
            if f == 0:
                fishday6and8 = fishperday[f]
            else:
                fishperday[f] -= fishdaycount
                fishperday[f-1] += fishdaycount
        fishperday[0] -= fishday6and8
        fishperday[6] += fishday6and8
        fishperday[8] += fishday6and8

    for f in range(len(fishperday)):
        totalfish += fishperday[f]
    
    return totalfish

if __name__ == "__main__":
    main('input.txt')