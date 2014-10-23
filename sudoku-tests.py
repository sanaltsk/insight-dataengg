"""
    This is a program to verify the functionality of sudoku.py

    input: csv file containing the sudoku unsolved matrix, whereever the values are blank or to
            be computed replace them with 0. Each value is seperated by commas and structured
            into 9x9 matrix.
    Execution : python sudoku-tests.py
                Enter CSV file name[data1.csv]: data2.csv

                On pressing enter key when asked to enter csv file name, it takes data1.csv by default
                One entering a file name, the verification of sudoku.py is performed on the
                newly entered csv file
"""
from sudoku import main,getColumnNumbers
import unittest

def getBoxNumbers(row,column):
    """
    Get the 9 number sqauare in the Sudoku matrix based on the row and column position

    :param row: the row coordinate
    :param column: the column coordinate
    :return:  list of numbers present small box(3x3 matrix) of the sudoku unsolved matrix with
                respect the the row and column provided
    """
    boxNumbers = []
    for i in range(0,3):
        for j in range(0,3):
            boxNumbers.append(matrix[i+row][j+column])
    return boxNumbers

class MyTest(unittest.TestCase):

    def test_rowCheck(self):
        """
        checks if the solved matrix rows have all the numbers from 1 to 9 each present once
        """
        for row in matrix:
            self.assertEquals(sorted(row),range(1,10))

    def test_columnCheck(self):
        """
        checks if the solved matrix columns have all the numbers from 1 to 9 each present once
        """
        for column in [getColumnNumbers(matrix,i) for i in xrange(9)]:
            self.assertEquals(sorted(column),range(1,10))

    def test_box(self):
        """
        checks if the solved matrix having 3x3 small boxes have all the numbers
        from 1 to 9 each present once
        """
        for row in xrange(0,8,3):
            for column in xrange(0,8,3):
                self.assertEquals(sorted(getBoxNumbers(row,column)), range(1,10))



if __name__=="__main__":
    inputfile = raw_input("Enter CSV file name[data.csv]:")
    if inputfile=='':
        inputfile='data1.csv'
    print 'Reading '+inputfile
    matrix = main(inputfile,inputfile[:-4]+"_output.csv")
    unittest.main()
