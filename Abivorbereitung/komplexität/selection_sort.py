from random import randint

def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = i
        
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
                
        
        array[i], array[min_index] = array[min_index], array[i]
    
    return array
        
lst = []

for i in range(10):
    lst.append(randint(0,100))
    
print('Unsortierte Liste')
print(lst)

print('Sortierte Liste')
print(selection_sort(lst))