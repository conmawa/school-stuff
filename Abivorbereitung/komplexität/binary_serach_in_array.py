from random import randint, choice

def binary_search(array, target):
    #array.sort()
    middle = len(array)//2
    left_array = array[0:middle]
    right_array = array[middle:]
    
    if target == array[middle]:
        print('gefunden')
        return True
    elif target < array[middle]:
        binary_search(left_array, target)
    elif target > array[middle]:
        binary_search(right_array, target)
        

lst = []
for i in range(10):
    lst.append(randint(0,100))

lst.sort()

binary_search(lst, choice(lst))