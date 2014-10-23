"""
    This is a program to solve inputed sudoku matrix.
    Input : csv file containing the sudoku unsolved matrix, whereever the values are blank or to
            be computed replace them with 0. Each value is seperated by commas and structured
            into 9x9 matrix.
    Output: Displays the solved sudoku matrix. The red values corresponds to the computed values
            and green values are the values suppiled in through the input. Output solved sudoku
            will be written to a file <<input-csv-filename>>_output.csv.

    Execution : python sudoku.py <<csv-filename>>

                python sudoku.py data.csv

    Sample Data: Six sample datasets are available(data1,data2...6) these sample sudoku matrices are
                of varying difficulty levels (taken from the internet)
"""

import csv
import sys
indexList=[]


def readCSV(file):
    """
    Function reads the inputted csv file to list
    :param file: csv-filename
    :return: returns the sudoku matrix read from the csv file
    """

    try:
        with open(file, 'r') as readfile:
            csvreader = csv.reader(readfile, delimiter=',')
            contents=[]
            for row in csvreader:
                contents.append([int(i) for i in row])
            return contents
    except:
        print file+" : File does not exist!"

def writeCSV(matrix,file):
    """
    Function writes the solved sudoku matrix to csv file
    :param matrix: solved sudoku matrix
    :param file: output csv-filename
    """
    try:
        with open(file, 'wb') as outputfile:
            csvwriter = csv.writer(outputfile)
            for row in matrix:
                csvwriter.writerow(row)
    except:
        print file+" : Error writing output to file!"

def solveSudokuMatrix(matrix):
    """
    This function searches for each 0 entry in the matrix(Blank element in sudoku) and
    iterates through 1 to 9 values for deducing the best match at the particular location.

    If a suitable value is matched the same function is recursively called with the updated value

    :param matrix: sudoku unsolved matrix
    :return: returns True if sudoku is successfully solved and False if not
    """

    row = 0
    col = 0
    flag,row,col = findNextBlankLocation(matrix,row,col)
    if not flag:
        return True

    for num in xrange(1,10):
        if isSafe(matrix,row,col,num):
            matrix[row][col] = num

            if solveSudokuMatrix(matrix):
                return True
            matrix[row][col]=0
    return False

def findNextBlankLocation(matrix,row,col):
    """
    This function searches for the next blank or 0 spot in the unsolved sudoku matrix

    :param matrix: sudoku unsolved matrix
    :param row: the current row coordinate
    :param col: the current column coordinate
    :returns: True,r,c where True is for successfully finding a blank spot or 0 and
             r,c are row and column for the blank spot

             False,r,c where False if it could not find any blank spot or 0 and
             r,c are the last values of row and column searched
    """

    r=0
    c=0
    for r in xrange(row,9):
        for c in xrange(col,9):
            if matrix[r][c]==0:
                indexList.append([r,c])
                return True,r,c
        # if 0 in matrix[r]:
        #     c=matrix[r].index(0)
        #     indexList.append([r,c])
        #     return True,r,c
    return False,r,c

def isSafe(matrix,row,col,num):
    """
    This function checks if its safe to populate a number, by verifying for any conflicts in
        row,column and box level with respect to the row and col inputted.

    :param matrix: unsolved sudoku matrix
    :param row:    the row coordinate where the 0 is to be replaced by num
    :param col:    the column coordinate where the 0 is to be replaced by num
    :param num:    the number that is being replaced at 0
    :return:       True, if the unsolved matrix can accommodate the new number without any coflicts in
                    row,column or box level
                   False, if the new number is already present in row,column or box levels
    """

    box = isNumberUsedInBox(matrix,row-row%3,col-col%3,num)
    column =  isNumberUsedInColumn(matrix,col,num)
    rows = isNumberUsedInRow(matrix,row,num)
    return not box and not column and not rows

def isNumberUsedInRow(matrix,row,num):
    """
    This is a helper function to isSafe function above. The function checks for the presence
        of the num in the unsolved sudoku matrix rows.

    :param matrix:  unsolved sudoku matrix
    :param row:     the row coordinate where the 0 is to be replaced by num
    :param num:     the number that is being replaced at 0
    :return:        True if num is present in the row of the sudoku unsolved matrix
                    False if num is not present in the inputted row
    """

    if num in matrix[row]:
        return True
    return False

def isNumberUsedInColumn(matrix,col,num):
    """
    This is a helper function to isSafe function above. The function checks for the presence
        of the num in the unsolved sudoku matrix columns.

    :param matrix:  sudoku unsolved matrix
    :param col:     the column coordinate where the 0 is to be replaced by num
    :param num:     the number that is being replaced at 0
    :return:        True if num is present in the column of the sudoku unsolved matrix
                    False if num is not present in the inputted column
    """

    if num in getColumnNumbers(matrix,col):
        return True
    return False

def getColumnNumbers(matrix,col):
    """
    This function returns the list of column elements of the unsolved sudoku matrix based
    col value. if col is 0,it returns the first column.

    :param matrix:  sudoku unsolved matrix
    :param col:     the column coordinate whose column is to be fetched
    :return:        List of column elements
    """

    columnNumbers = []
    for row in matrix:
        columnNumbers.append(row[col])
    return columnNumbers

def isNumberUsedInBox(matrix,boxStartRow,boxStartCol,num):
    """
    This is a helper function to isSafe function above. The function checks for the presence
    of the num in the unsolved sudoku matrix small boxes (3x3 matrix).

    :param matrix: unsolved sudoku matrix
    :param boxStartRow: starting row coordinate of the box(3x3 matrix)
    :param boxStartCol: starting column coordinate of the box(3x3 matrix)
    :param num: The propesed number to be replaced in the blank space
    :return: True if num is present in the small box(3x3 matrix) of the sudoku unsolved matrix
             False if num is not present in the inputted small box(3x3 matrix)
    """
    for row in xrange(3):
        for col in xrange(3):
            if matrix[row+boxStartRow][col+boxStartCol]==num:
                return True
    return False

def printMatrix(matrix):
    """
        This function prints out the inputted sudoku matrix, the solved values are print in red
        and the values which were present in the unsolved sudoku matrix are print in green

        :param matrix: sudoku matrix
    """
    redBoldFont = '\033[31;1m'
    greenFont = '\033[32m'
    endofline = '\033[0m'

    for row in xrange(9):
        for col in xrange(9):
            if [row,col] in indexList:
                print redBoldFont +str(matrix[row][col]) + endofline,
            else:
                print greenFont +str(matrix[row][col]) + endofline,
        print ''



def main(inputfile,outputfile):
    """
    This is the main driver function
    :param file: csv file-name
    :return : sudoku matrix
    """
    matrix = readCSV(inputfile)
    if matrix:
        if solveSudokuMatrix(matrix):
            print "Solved Sudoku"
            printMatrix(matrix)
            print "Solved Sudoku written to file : " + outputfile
            writeCSV(matrix,outputfile)
        else:
            print "No Solution"
        return matrix


#  The program starts by accepting an argument - csv filename
if __name__ == "__main__":
    if len(sys.argv)==2:
        file=sys.argv[1]
        main(file,file[:-4]+"_output.csv")
    else:
        print 'Usage:  python sudoku.py <<input-csv-file>>\n\tpython sudoku.py data.csv'

        print """the <<input-csv-file>> should contain 9x9 matrix of numbers seperated by comma,
"and zero in places where the value is to be solved for. The output file will be generated as
<<input-csv-file>>_output.csv consisting the solved sudoku matrix"""
