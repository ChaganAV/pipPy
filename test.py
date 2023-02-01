m = ['*', 'X', 'X', 'X', 'X', 'X', '*', '*', '*']
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

print(checkRow())