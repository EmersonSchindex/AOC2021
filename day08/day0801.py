def main(f):
    with open(f, "r") as file1:
        lines = [(line.strip()).split('|') for line in file1 if line.strip()]

#    print(part1(lines))
    print(part2(lines))

def part1(lines):

    numberofcodes = 0
    
    for l in range(len(lines)):
        teststring = lines[l]
        teststring[1].split(',')
        for code in teststring[1].split(" "):
            if len(code) in(2, 3, 4, 7):
                numberofcodes += 1

    return numberofcodes

def part2(lines):  # sourcery no-metrics

    codes = ""
    sumofcodes = 0
    
    for l in range(len(lines)):
        teststring = lines[l]
        teststring[1].split(',')
        codes = " "
        for code in teststring[1].split(" "):
            if len(code) == 2:
                codes += "1"
            elif len(code) == 3:
                codes += "7"
            elif len(code) == 4:
                codes += "4"
            elif len(code) == 7:
                codes += "8"
            elif len(code) == 5 and "g" in code:
                codes += "2"
            elif len(code) == 5 and "a" in code and "d" in code:
                codes += "3"
            elif len(code) == 5 and "d" in code and "e" in code:
                codes += "5"
            elif len(code) == 6 and "g" in code:
                codes += "6"
            elif len(code) == 6 and "a":
                codes += "3"
            elif len(code) == 5 and "a" in code and "g" in code:
                codes += "0"
            
#        print(codes)    
        
        sumofcodes += int(codes)

    return sumofcodes

if __name__ == "__main__":
    main('input.txt')