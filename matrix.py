def showMatrix():
    print(matrix[0],matrix[1],matrix[2])
    print(matrix[3],matrix[4],matrix[5])
    print(matrix[6],matrix[7],matrix[8])

def checkWin():
    res = 0
    if matrix[0] == matrix[1] == matrix[2] == '0' or matrix[0] == matrix[1] == matrix[2] == 'X':
        print(f'Победили {matrix[0]}')
        res = 1
    if matrix[3] == matrix[4] == matrix[5] == '0' or matrix[3] == matrix[4] == matrix[5] == 'X':
        print(f'Победили {matrix[3]}')
        res = 1
    if matrix[6] == matrix[7] == matrix[8] == '0' or matrix[0] == matrix[1] == matrix[2] == 'X':
        print(f'Победили {matrix[6]}')
        res = 1
    if matrix[0] == matrix[3] == matrix[4] == '0' or matrix[0] == matrix[3] == matrix[4] == 'X':
        print(f'Победили {matrix[0]}')
        res = 1
    if matrix[1] == matrix[4] == matrix[7] == '0' or matrix[1] == matrix[4] == matrix[7] == 'X':
        print(f'Победили {matrix[1]}')
        res = 1
    if matrix[2] == matrix[5] == matrix[8] == '0' or matrix[2] == matrix[5] == matrix[8] == 'X':
        print(f'Победили {matrix[2]}')
        res = 1
    if matrix[0] == matrix[4] == matrix[8] == '0' or matrix[0] == matrix[4] == matrix[8] == 'X':
        print(f'Победили {matrix[0]}')
        res = 1
    if matrix[2] == matrix[4] == matrix[6] == '0' or matrix[2] == matrix[4] == matrix[6] == 'X':
        print(f'Победили {matrix[2]}')
        res = 1
    return res

matrix = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
showMatrix()
while True:
    number = int(input("Введите номер ячейки, чтобы поставить крестик: "))
    matrix[number-1] = 'X'

    showMatrix()
    res = checkWin()
    if res == 1:
        break
