transtable =  {
    '0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6', '0111':'7', 
    '1000':'8', '1001':'9', '1010':'A', '1011':'B', '1100':'C', '1101':'D', '1110':'E', '1111':'F'
    }

'''
3 bits V (110)   are packet version, 6.
3 bits T (100)   are packet type ID, 4 i.e. packet is a literal value.
5 bits A (10111) start with a 1 (not the last group, keep reading) and contain the first four bits of the number, 0111.
5 bits B (11110) start with a 1 (not the last group, keep reading) and contain four more bits of the number, 1110.
5 bits C (00101) start with a 0 (last group, end of packet) and contain the last four bits of the number, 0101.

3 unlabeled 0 bits at the end are extra due to the hexadecimal representation and should be ignored.
'''

def splitpackage(binpackage):
    s = 1
    
    # decpackage = int('110', 2) # bin to dec conversion

    # all fixed based on first example. How to make a dynamic function for this?
    V = binpackage[:3]
    V = int(V, 2)

    T = binpackage[3:6]
    T = int(T, 2)

    A = binpackage[7:10]
    A = int(A, 2)
    
    return s

def main(f):
    # keep for later to read in file
    """     transtable = {}
    for line in open(f, 'r').readlines():
        (k, v) = line.strip().split(' = ')
        transtable[k] = v
    """      
    
    hexpackage = 'D2FE28'
    
    binpackage = bin(int(hexpackage, 16))[2:].rstrip('0') # already remove the trainling zeros
    
    # add code to split binpackage in chuncks accoring to above rules
    # use the transtable
    s = splitpackage(binpackage)        

    print(binpackage, len(binpackage))

if __name__ == '__main__':   
    main('input.txt') 