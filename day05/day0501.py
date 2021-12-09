def main(f):
    with open(f, "r") as file1:
        lines = [(line.strip()).split() for line in file1 if line.strip()]

#    print(part1(lines))
    print(part2(lines))

def part1(lines):  # sourcery no-metrics
    number1 = 0
    number2 = 0
    number3 = 0
    number4 = 0
    aantal = 0
    result = 0
    nummatrix = [[0 for col in range(1000)] for row in range(1000)]

    for r in range(len(lines)):
        result = lines[r][0].index(',')
        number1 = int(lines[r][0][:result])
        number2 = int(lines[r][0][result + 1 : len(lines[r][0])])
        result = lines[r][2].index(',')
        number3 = int(lines[r][2][:result])
        number4 = int(lines[r][2][result + 1 : len(lines[r][2])])

        if number1 == number3:
            if number2 >= number4:
                for n1 in range(number4, number2 + 1):
                    nummatrix[n1][number1] += 1
            else:
                for n2 in range(number2, number4 + 1):
                    nummatrix[n2][number1] += 1

        if number2 == number4:
            if number1 >= number3:
                for n3 in range(number3, number1 + 1):
                    nummatrix[number2][n3] += 1
            else:
                for n4 in range(number1, number3 + 1):
                    nummatrix[number2][n4] += 1

    for item in nummatrix:
        for n in range(len(item)):
            if item[n] >= 2:
                aantal += 1

    return aantal
    
def part2(lines):
    teller3 = 0
    teller4 = 0
    teller5 = 0
    teller6 = 0
    number1 = 0
    number2 = 0
    number3 = 0
    number4 = 0
    aantal = 0
    result = 0
    nummatrix = [[0 for col in range(1000)] for row in range(1000)]

    for r in range(len(lines)):
        result = lines[r][0].index(',')
        number1 = int(lines[r][0][:result])
        number2 = int(lines[r][0][result + 1 : len(lines[r][0])])
        result = lines[r][2].index(',')
        number3 = int(lines[r][2][:result])
        number4 = int(lines[r][2][result + 1 : len(lines[r][2])])

        if number1 == number3:
            if number2 >= number4:
                for n1 in range(number4, number2 + 1):
                    nummatrix[n1][number1] += 1
            else:
                for n2 in range(number2, number4 + 1):
                    nummatrix[n2][number1] += 1

        if number2 == number4:
            if number1 >= number3:
                for n3 in range(number3, number1 + 1):
                    nummatrix[number2][n3] += 1
            else:
                for n4 in range(number1, number3 + 1):
                    nummatrix[number2][n4] += 1

        if number1 > number3:
            if number2 > number4:
                teller3 += 1
                v11 = 0
                for _ in range(number3, number1 + 1):
                    nummatrix[number4 + v11][number3 + v11] += 1
                    v11 += 1
            if number2 < number4:
                teller4 += 1
                v12 = 0
                for _ in range(number3, number1 + 1):
                    nummatrix[number2 + v12][number1 - v12] += 1
                    v12 += 1

        if number1 < number3:
            if number2 > number4:
                teller5 += 1
                v13 = 0
                for v1 in range(number1, number3 + 1):
                    nummatrix[number2 - v13][number1 + v13] += 1
                    v13 += 1
            if  number2 < number4:
                teller6 += 1
                v14 = 0
                for v1 in range(number1, number3 + 1):
                    nummatrix[number2 + v14][number1 + v14] += 1
                    v14 += 1

#        print(number1, end = " ")
#        print(number2, end = " ")
#        print(number3, end = " ")
#        print(number4)
    
    for item in nummatrix:
        for n in range(len(item)):
            if item[n] >= 2:
                aantal += 1

#    print(teller3)
#    print(teller4)
#    print(teller5)
#    print(teller6)
    return aantal

if __name__ == "__main__":
    main('input.txt')