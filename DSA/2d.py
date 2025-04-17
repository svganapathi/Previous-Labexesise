import sys
def pascal(col,row):
    if(col == 0) or (col == row):
        return 1
    else:
        return pascal(col-1,row-1) + pascal(col,row-1)
def PascalTriangle(num):
    if (num <= 0):
        print('Number must be greater than zero')
    for r in range(num):
        for c in range(r+1):
            sys.stdout.write(str(pascal(c,r))+' ')
        sys.stdout.write('\n')
PascalTriangle(4)