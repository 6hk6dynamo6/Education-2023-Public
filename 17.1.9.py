def sort():
    for i in range(len(L)):
        for j in range(len(L) - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L

def binary_search(L, A, left, right):
    if left > right:  # если левая граница превысила правую,
        return "Введено число не входящее последовательность"  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if L[middle] == A:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif A < L[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(L, A, left, middle - 1)
    else:  # иначе в правой
        return binary_search(L, A, middle + 1, right)

L = list(map(int, input("Введите, пожалуйста, последовательность чисел через пробел   ").split()))
print(sort())

A = int(input("Введите любое число "))

print(binary_search(L, A, 0, len(L)-1))

