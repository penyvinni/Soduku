from PencilMark import CmdMarking
import math
from ortools.sat.python import cp_model


def Input(filename):
    with open('inputdata.txt', 'r') as f:
        for sudoku in f:
            content=f.read()
            list=content.split()


    return list




def ToBoard(rawdata: str) -> list:
    if rawdata == '':
        return list()
    gridsize = int(math.sqrt(len(rawdata)))
    substrs = list()
    start = 0
    next = gridsize
    while next <= len(rawdata):
        substrs.append(rawdata[start:next])
        start = next
        next += gridsize
    return substrs





def Formatter(sudokustr):
    if sudokustr == '':
        return
    data = ToBoard(sudokustr)
    print(str("." + "-" * 6 + "") * 3, end="")
    print(".")
    counter = 0
    for x in data:
        if counter % 3 == 0 and counter != 0:
            print(":", end="")
            print("------ " * 2, end="")
            print("------:")
        print("|", end="")
        for j in range(0, len(x), 3):
            print(
                str(x[j]) if x[j] != "0" else ".",
                str(x[j + 1]) if x[j + 1] != "0" else ".",
                str(x[j + 2]) if x[j + 2] != "0" else ".",
                "|",
                end="",
            )
        print()
        counter += 1
    print(str("." + "-" * 6 + "") * 3 + ".")



def pencilMark(data):
    CmdMarking(data)



def SolveSudoku(sudokuString):
    data = ToBoard(sudokuString)
    model = cp_model.CpModel()
    pos = dict()
    range9 = range(0, 9)
    for row in range9:
        for col in range9:
            if int(data[row][col]) != 0:
                pos[row, col] = int(data[row][col])
            else:
                pos[row, col] = model.NewIntVar(1, 9, f'pos[{row}][{col}]')

    for row in range9:
        model.AddAllDifferent([pos[row, col] for col in range9])

    for col in range9:
        model.AddAllDifferent([pos[row, col] for row in range9])

    for rowid in range(0, 9, 3):
        for colid in range(0, 9, 3):
            model.AddAllDifferent(
                [
                    pos[row, col] 
                    for col in range(colid, (colid+3)) 
                    for row in range(rowid, (rowid+3))
                ]
            )

    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    result = ''
    if status == cp_model.OPTIMAL:
        for row in range9:
            for col in range9:
                result += str(solver.Value(pos[row, col]))

    return result
