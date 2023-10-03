def sortfunc(line):
    array = line.split()
    for i in range(len(array)):
        array[i] = int(array[i])
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
    return str(array)[1:-1]