def main(f):
    coords, folds = open(f).read().split('\n\n')
    coords = [(int(dot.split(',')[0]), int(dot.split(',')[1])) for dot in coords.splitlines()]
    folds = [(axis[-1], int(val)) for fold in folds.splitlines() for axis, val in [fold.split('=')]]

    axis, foldline = folds[0]
    sum = 0

    for i, (x, y) in enumerate(coords):
        if axis == 'x' and x < foldline:
            sum += 1

        if axis == 'x' and x > foldline:
            c1 = coords[i]
            c2 = (foldline - (c1[0] - foldline), c1[1])
            
            if c2 not in coords:
                sum+=1

        if axis == 'y' and y < foldline:
            sum += 1
        
        if axis == 'y' and y > foldline:
            c1 = coords[i]
            c2 = (c1[0], foldline - (c1[1] - foldline))
            
            if c2 not in coords:
                sum+=1

    print(sum)

if __name__ == '__main__':   
    main('input.txt')