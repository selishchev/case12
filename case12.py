import os
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
        print(my_files)

def main_findFiles():
    target = input('Введите элемент названия:')
    path = input('Введите имя каталога:')
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
        dir = os.path.abspath(os.curdir)
        print(dir)
    #elif x == 2:
        #moveUp()
    #elif x == 3:
        #moveDown()
   # elif x == 4:
        #countFiles()
    #elif x == 5:
        #countBytes()
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


main()
