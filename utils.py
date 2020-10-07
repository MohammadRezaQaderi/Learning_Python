
def find_max(array):
    maximum = array[0]
    for element in array:
        if element > maximum:
            maximum = element
    return maximum        

