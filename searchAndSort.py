def binarySearch (item, my_list):
    found = False
    first = 0
    last = len(my_list) - 1

    while first <= last and found == False:
        midpoint = (first + last) / 2
        if my_list[midpoint] == item:
            found = True
        else:
            if my_list[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found

def bubbleSort(my_list):
    swap_again = True
    n = len(my_list)
    while n > 0 and swap_again == True:
        n = n - 1
        swap_again = False

        for i in range(n):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                swap_again = True
    return my_list

def insertionSort(my_list):
    n = len(my_list)
    for i in range (1, n):
        value = my_list[i]
        j = i
        while j > 0 and value < my_list[j - 1]:
            my_list[j] = my_list[j - 1]
            j = j - 1
        my_list[j - 1] = value
    return my_list