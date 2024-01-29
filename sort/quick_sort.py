from random import randint

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [x for x in array[1:] if x <= pivot]
        greater_than_pivot = [x for x in array[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

            

lst = []

for i in range(10000):
    lst.append(randint(0,10000))
    
print(quick_sort(lst))