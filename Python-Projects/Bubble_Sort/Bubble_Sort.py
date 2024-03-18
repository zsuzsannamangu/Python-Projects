#Bubble sort is a sorting algorithm that works by iterating through an array, and if any values
#are out of order, swaping them, then repeating the process until the array is in numerical order.

def bubblesort(elements):
    swapped = False
    # Looping from size of array from last index[-1] to index [0], so moving from back to front
    for n in range(len(elements)-1, 0, -1): #syntax: range(start, stop, step)
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                # swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]        
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return
 
elements = [39, 12, 18, 85, 72, 10, 2, 18]
 
print("Unsorted list:")
print(elements)
bubblesort(elements)
print("Sorted Array:")
print(elements)
