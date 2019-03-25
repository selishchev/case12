import os
import os.path

def moveUp():
    a = os.getcwd()
    b = os.path.split(a)
    os.chdir(b[0])
    print(os.getcwd())


def moveDown(currentDir):
    Dir = os.getcwd()
    a = os.path.join(Dir, currentDir)
    if os.path.exists(a):
        b = os.path.join(Dir, currentDir)
        os.chdir(b)
        print(os.getcwd())
    else:
        print('Ошибка')

n = int(input())
if n == 1:
    moveUp()
elif n == 2:
    a = input()
    moveDown(a)
