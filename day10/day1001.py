def main(f):
    with open(f, "r") as file1:
        lines = [(line.strip()).split('|') for line in file1 if line.strip()]

    print(part1(lines))

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
            if len(openstack) > 0 and openstack[-1] == openlist[pos]:
                openstack.pop()
                closestack.pop()
            else:
                closestack.append(c)
    return closestack


if __name__ == "__main__":
    main('input.txt')