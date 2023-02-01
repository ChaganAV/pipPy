from random import randint
def showMatrix():
    return f"{m[0]}{m[1]}{m[2]}\n{m[3]}{m[4]}{m[5]}\n{m[6]}{m[7]}{m[8]}"

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

def play(num):
    number = int(num)
    res = False
    if m[number-1] != '*':
        res = False
    else:
        m[number-1] = 'X'
        res = True
    return res
def insertRandom():
    while True:
        num = randint(0,8)
        if m[num] == '*':
            m[num] = '0'
            break
