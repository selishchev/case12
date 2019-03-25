import os
import os.path


def countFiles(path=os.getcwd()):
    sum = 0
    for i, j, k in os.walk(path):
        sum += len(k)
    print(sum)
    return sum


def countBytes(path=os.getcwd()):
    bytes = 0
    for i, j, k in os.walk(path):
        for p in k:
            if os.path.isfile(i + '/' + p):
                bytes += os.path.getsize(i + '/' + p)
    print(bytes)
    return bytes


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
        print()
        print('Ошибка! такой папки не существует!')
        print()


MENU = '1. Просмотр каталога'+'\n'+'2. На уровень вверх'+'\n'\
 '3. На уровень вниз'+'\n'+'4. Количество файлов и каталогов'+'\n'\
 '5. Размер текущего каталога (в байтах)'+'\n'+'6. Поиск файла'+'\n'\
 '7. Выход из программы'
QUIT = 7


def findFiles(target, path):
    my_files = []
    for dirs, sub, fil in os.walk(path):
        for x in fil:
            if target in x:
                my_files.append(os.path.abspath(os.path.join(dirs, x)))
    if len(my_files) == 0:
        print('Файла не существует! проверьте вводимые данные!')
    else:
        print()
        print("Файлы каталога [" + path + "], которые содержат подстроку '" + target + "':")
        for f in my_files:
            print("  ---> " + f)
        print("******************* КОНЕЦ ПОИСКА ФАЙЛОВ **********************************")


def main_findFiles():
    print("******************* ПОИСК ФАЙЛОВ **********************************")
    target = input('Введите часть названия файла:')
    path = input('Введите имя каталога, с которого начинать поиск:')
    findFiles(target, path)


def acceptCommand():
    check1 = False
    while not check1:
        try:
            x = int(input("Выберите номер команды:"))
            return x
        except ValueError:
            check1 = False
            print("Введите номер!")


def runCommand(x):
    if x == 1:
        files = os.listdir(os.getcwd())
        print()
        print("Содержимое каталога " + os.getcwd() + ":")
        for f in files:
            print("  ---> " + f)
    elif x == 2:
        moveUp()
    elif x == 3:
        moveDown(input("Введите название подкаталога:"))
    elif x == 4:
        countFiles()
    elif x == 5:
        countBytes()
    elif x == 6:
        main_findFiles()
    elif x == 7:
        return x


def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Работа программы завершена.")
            break


if __name__ == '__main__':
    main()
