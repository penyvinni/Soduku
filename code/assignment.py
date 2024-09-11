from sudoku import *

def main():
    inputdata = Input('inputdata.txt')
    for sudoku in inputdata:
        print(f'\nSequence used:{sudoku}\n')
        print('Preview \n')
        Formatter(sudoku)
        print()
        print('\n Marking \n')
        pencilMark(sudoku)
        print()
        print('\n Solution \n')
        solutiontoproblem = SolveSudoku(sudoku)
        Formatter(solutiontoproblem)
        print(f'\n Solution as string is:{solutiontoproblem}\n')
        print('\n--------------------------------------------------------------------\n')


if __name__ == "__main__":
    main()
