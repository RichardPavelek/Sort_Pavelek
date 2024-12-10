import random

#Pole s 10 náhodnými čísly
print("Seřazované pole")
array = []
for i in range(10):
    array.append(random.randint(0, 100))
print(array)

print()

#Bubble sort
print("Seřazení pomocí bubble sortu")
for i in range(len(array)):
    for j in range(len(array) - 1):
        if array[j] > array[j + 1]:
            # Prohození hodnot
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp

print(array)

print()

#Bogo sort
print("Seřazení pomocí bogo sortu")
def bogo_sort(array):
    while True:
        #Když není seřazeno hodnoty se zamíchají
        sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                sorted = False
                break
        if sorted:
            break
        #Zamíchání
        for i in range(len(array)):
            j = random.randint(0, len(array) - 1)
            array[i], array[j] = array[j], array[i]
    return array
print(bogo_sort(array))

print()

#Selection Sort
print("Seřazení pomocí selection sortu")
for i in range(len(array)):
    min = i
    for j in range(i + 1, len(array)):
        if array[j] < array[min]:
            min = j
    #Proházení
    temp = array[i]
    array[i] = array[min]
    array[min] = temp
print(array)

print()

#Insertion Sort
print("Seřazení pomocí insertion sort")
for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key
print(array)
