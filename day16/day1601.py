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
    versionsum = 0
#   Every packet begins with a standard header: 
#   the first three bits encode the packet version, 
#   and the next three bits encode the packet type ID. 
#   These two values are numbers; 
#   all numbers encoded in any packet are represented as binary with the most significant bit first.     
    
    for b in range(len(binpackage)):
#        totallength = len(binpackage)
        version = int(binpackage[:3], 2)
        type = int(binpackage[3:6], 2)
    
# next read action is dependent on the value of type:
# if the type == 4; then a number of literal values follow
# if these start with a one there will be at least another one
# if these start with a zero it indicates the last one
# so each value has 5 bits, a leading 1 or 0 and 4 bits for the value
# the total lenght of the package will be a multiple of 4 bits
# any type othr than 4, indicates an operator
# an operator package contains one or more packages
# there are 2 modes to determine the number of packes:
# if the bit immediately after the header is equal to zero, then the next 15 bits
# are a number which represents the total length in bits of the subpackages contained
# if the bit immediately after the header is equal to 1, then the next 11 bits
# are the number of packages

        if type != 4:
            if int(binpackage[6]) == 0:
                bitlength = int(binpackage[7:23], 2)
            if int(binpackage[6]) == 1:
                numofpackages = int(binpackage[7:18], 2)
    
        if type == 4:
            binrep = ''
            nextindicator = int(binpackage[6])
            binrep += binpackage[7:11]

    
    return versionsum

def main(f):
# keep for later to read in file
    sum = 0
    file = open(f, 'r')
    lines = file.read().strip().splitlines()
    hexpackage = str(lines[0])

#    hexpackage = 'D2FE28'
    
    binpackage = bin(int(hexpackage, 16))[2:]
#    binpackage = bin(int(hexpackage, 16))[2:].rstrip('0') # already remove the trainling zeros
    
    # add code to split binpackage in chuncks accoring to above rules
    # use the transtable
    sum = splitpackage(binpackage)        

    print(binpackage, len(binpackage))

if __name__ == '__main__':   
    main('input.txt') 