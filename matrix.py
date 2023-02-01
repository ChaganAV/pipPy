def showMatrix():
    print(m[0],m[1],m[2])
    print(m[3],m[4],m[5])
    print(m[6],m[7],m[8])
def outMatrix():
    return f"{m[0]}{m[1]}{m[2]}\n{m[3]}{m[4]}{m[5]}\n{m[6]}{m[7]}{m[8]}"

def checkWin2():
    res = 0
    if m[0] == m[1] == m[2] == '0' or m[0] == m[1] == m[2] == 'X':
        print(f'Победили {m[0]}')
        res = 1
    if m[3] == m[4] == m[5] == '0' or m[3] == m[4] == m[5] == 'X':
        print(f'Победили {m[3]}')
        res = 1
    if m[6] == m[7] == m[8] == '0' or m[0] == m[1] == m[2] == 'X':
        print(f'Победили {m[6]}')
        res = 1
    if m[0] == m[3] == m[4] == '0' or m[0] == m[3] == m[4] == 'X':
        print(f'Победили {m[0]}')
        res = 1
    if m[1] == m[4] == m[7] == '0' or m[1] == m[4] == m[7] == 'X':
        print(f'Победили {m[1]}')
        res = 1
    if m[2] == m[5] == m[8] == '0' or m[2] == m[5] == m[8] == 'X':
        print(f'Победили {m[2]}')
        res = 1
    if m[0] == m[4] == m[8] == '0' or m[0] == m[4] == m[8] == 'X':
        print(f'Победили {m[0]}')
        res = 1
    if m[2] == m[4] == m[6] == '0' or m[2] == m[4] == m[6] == 'X':
        print(f'Победили {m[2]}')
        res = 1
    return res
def check(x,y,z):
    return x==y==z

def checkRow():
    if check(m[0],m[1],m[2]): return m[0]
    if check(m[3],m[4],m[5]): return m[3]
    if check(m[6],m[7],m[8]): return m[6]
    if check(m[0],m[3],m[6]): return m[0]
    if check(m[1],m[4],m[7]): return m[1]
    if check(m[2],m[5],m[8]): return m[2]
    if check(m[0],m[4],m[8]): return m[0]
    if check(m[2],m[4],m[6]): return m[2]
    return '*'

m = ['*', '*', '*', '*', '*', '*', '*', '*', '*']

# showm()

def play1(num):
    while True:
        # number = int(input("Введите номер ячейки, чтобы поставить крестик: "))
        number = int(num)
        m[number-1] = 'X'

        # showm()
        resOut = outMatrix()
        res = checkWin2()
        if res == 1:
            break
def play(num):
    # number = int(input("Введите номер ячейки, чтобы поставить крестик: "))
    number = int(num)
    m[number-1] = 'X'

    # showm()
    res = outMatrix()
    # res = checkWin()
    return res
