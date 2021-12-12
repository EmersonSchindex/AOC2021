import math

def main(f):
    with open(f, "r") as file1:
        lines = [(line.strip()).split('|') for line in file1 if line.strip()]

    print(part1(lines))
    print(part2(lines))

def part1(lines):
    errorscore = 0
    for l in range(len(lines)):
        stack = []
        regel = str(lines[l])
        regel = regel[2:len(regel)-2]
        stack = check_balance(regel)
        if len(stack) > 1:
            if stack[0] == ")":
                errorscore += 3
            elif stack[0] == "]":
                errorscore += 57
            elif stack[0] == "}":
                errorscore += 1197
            elif stack[0] == ">":
                errorscore += 25137    

    return errorscore

def check_balance(expression):
    openlist = ['(', '[', '{', '<']
    closelist = [')', ']', '}', '>']
    openstack = []
    closestack = []
    for c in expression:
        if c in openlist:
            openstack.append(c)
        elif c in closelist:
            closestack.append(c)
            pos = closelist.index(c)
            if openstack and openstack[-1] == openlist[pos]:
                openstack.pop()
                closestack.pop()
            else:
                closestack.append(c)

    return closestack

def check_balance2(expression):
    openlist = ['(', '[', '{', '<']
    closelist = [')', ']', '}', '>']
    score = 0
    openstack = []
    closestack = []
    for c in expression:
        if c in openlist:
            openstack.append(c)
        elif c in closelist:
            closestack.append(c)
            pos = closelist.index(c)
            if openstack and openstack[-1] == openlist[pos]:
                openstack.pop()
                closestack.pop()
            else:
                closestack.append(c)

    if not closestack:
        openstack.reverse()
        points = [1, 2, 3, 4]
        for c in openstack:
            pos = openlist.index(c)
            score = (score * 5) + points[pos]

    return score

def part2(lines):
    totalscore = []
    totalscore2 = []
    newlines = []
    balance = 0
    finalscore = 0
    for l in range(len(lines)):
        stack = []
        regel = str(lines[l])
        regel = regel[2:len(regel)-2]
        balance = check_balance2(regel)
        if balance > 0:
            totalscore.append(balance)

    totalscore2 = sorted(totalscore)
    midvalue = math.floor(len(totalscore2) / 2)
    finalscore = totalscore2[midvalue]

#    print(midvalue)

#    print(finalscore)
    return finalscore

if __name__ == "__main__":
    main('input.txt')