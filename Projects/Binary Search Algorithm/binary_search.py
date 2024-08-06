def binary_search(data, element):
    #sorting list before using the binary search algorithm
    data.sort()

    #declare variables
    steps = 0
    start = 0
    middle = 0
    end = len(data)

    while(start <= end):
        #display step with current list after each step
        print("Step:", steps, " - ", str(data[start:end+1]))
        steps+=1
        middle = (start + end) // 2

        if element == data[middle]:
            return middle
        if element < data[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1
