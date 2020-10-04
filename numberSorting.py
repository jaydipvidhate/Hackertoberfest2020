def sort(numbers):
    swapped=True
    while swapped:
        swapped=False
        for i in range(len(numbers) -1):
            if numbers[i]>numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
                swapped=True
                
list=[1,4,2,7,4,9,5,100]
print("unsorted list",list)
sort(list)
print("Sorted list",list)