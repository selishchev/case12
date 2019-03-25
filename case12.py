import os


def countFiles(path=os.getcwd()):
    sum = 0
    for i, j, k in os.walk(path):
        sum += len(k)
    return sum


def countBytes(path=os.getcwd()):
    bytes = 0
    for i, j, k in os.walk(path):
        for p in k:
            if os.path.isfile(i + '/' + p):
                bytes += os.path.getsize(i + '/' + p)
    return bytes


print(countFiles())
print(countBytes())
