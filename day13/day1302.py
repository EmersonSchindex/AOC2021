def main(f):
    coords, folds = open(f).read().split('\n\n')
    coords = [(int(dot.split(',')[0]), int(dot.split(',')[1])) for dot in coords.splitlines()]
    folds = [(axis[-1], int(val)) for fold in folds.splitlines() for axis, val in [fold.split('=')]]

    sum = 0
    matrix = [[0 for col in range(51)] for row in range(51)]

    for f in range(len(folds)):
        axis, foldline = folds[f]  
        for i, (x, y) in enumerate(coords):
            if axis == 'x' and x < foldline:
                sum += 1

            if axis == 'x' and x > foldline:
                c1 = coords[i]
                c2 = (foldline - (c1[0] - foldline), c1[1])
            
                if c2 not in coords:
                    sum+=1
                
                coords[i] = c2

            if axis == 'y' and y < foldline:
                sum += 1
        
            if axis == 'y' and y > foldline:
                c1 = coords[i]
                c2 = (c1[0], foldline - (c1[1] - foldline))
            
                if c2 not in coords:
                    sum+=1

                coords[i] = c2

        if f == 0:
            print(sum)
    
    print('\n'.join(''.join('▓' if (x, y) in coords else ' ' for x in range(40)) for y in range(6)), sum)
#    for c in range(len(coords)):
##        x = coords[c][0]
#        y = coords[c][1]
#        matrix[x][y] = 1
#
#    for m in range(len(matrix)):
#        print(matrix[m])
    

if __name__ == '__main__':   
    main('input.txt')