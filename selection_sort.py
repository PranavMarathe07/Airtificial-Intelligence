def selectionSort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

print("Enter the length of the array:")
num = int(input())

array = []
for i in range(num):
    print("Enter a number:")
    number = int(input())
    array.append(number)

print(selectionSort(array))