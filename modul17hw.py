numbers = input("Введите последовательность чисел через пробел:").split()
try:
    number =int(input("Введите число: "))
    numlist = list(map(int, numbers))
except ValueError:
    print("Ошибка ввода данных. Выход из программы.")
    exit()
else:
    pass

for i in range(1, len(numlist)):
    x = numlist[i]
    idx = i
    while idx > 0 and numlist[idx-1] > x:
        numlist[idx] = numlist[idx-1]
        idx -= 1
    numlist[idx]  = x
print(numlist)

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] < element and array[middle+1] >= element:
       return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
#Необходимо переписать это условие, чтоб условие искало число, которое меньше введенного числа а следующее за ним больше или равен этому числу


#Если условие выполнится, то возвращаем индекс middle - 1
array = numlist
element = number
print(binary_search(array, element, 0, numlist[-1]))