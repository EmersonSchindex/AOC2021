def main(f):
    with open(f, "r") as file1:
        lines = [(line.strip()).split('|') for line in file1 if line.strip()]

    print(part1(lines))
#    print(part2(lines))

def part1(lines):

    regel = " "
    regelonder = " "
    regelboven = " "
    risklevel = 0

    for l in range(len(lines)):
        regel = str(lines[l])
        lengte = len(regel)
        if l == 0:
            regelonder = str(lines[l+1])
        elif l == len(lines) - 1:
            regelboven = str(lines[l-1])
        else:
            regelonder = str(lines[l+1])
            regelboven = str(lines[l-1])

        for n in range(2, len(regel) - 2):
            if l == 0:
                if n == 2:
                    if regel[n] < regel[n +1] and regel[n] < regelonder[n]:
                        risklevel += int(regel[n]) + 1
                if n > 2 and n < len(regel) - 3:
                    if regel[n] < regel[n + 1] and regel[n] < regel[n - 1] and regel[n] < regelonder[n]:
                        risklevel += int(regel[n]) + 1
                if n == len(regel) - 3:
                    if regel[n] < regel[n - 1] and regel[n] < regelonder[n]:
                        risklevel += int(regel[n]) + 1

            elif l == len(lines) - 1:
                if n == 2:
                    if regel[n] < regel[n +1] and regel[n] < regelboven[n]:
                        risklevel += int(regel[n]) + 1
                if n > 2 and n < len(regel) - 3:
                    if regel[n] < regel[n + 1] and regel[n] < regel[n - 1] and regel[n] < regelboven[n]:
                        risklevel += int(regel[n]) + 1
                if n == len(regel) - 3:
                    if regel[n] < regel[n - 1] and regel[n] < regelboven[n]:
                        risklevel += int(regel[n]) + 1
            else:
                if n == 2:
                    if regel[n] < regel[n +1] and regel[n] < regelonder[n] and regel[n] < regelboven[n]:
                        risklevel += int(regel[n]) + 1
                if n > 2 and n < len(regel) - 3:
                    if regel[n] < regel[n + 1] and regel[n] < regel[n - 1] and regel[n] < regelonder[n] and regel[n] < regelboven[n]:
                        risklevel += int(regel[n]) + 1
                if n == len(regel) - 3:
                    if regel[n] < regel[n - 1] and regel[n] < regelonder[n] and regel[n] < regelboven[n]:
                        risklevel += int(regel[n]) + 1

    return risklevel

def part2(lines):  # sourcery no-metrics

    sumofcodes = 0

    return sumofcodes

if __name__ == "__main__":
    main('input.txt')