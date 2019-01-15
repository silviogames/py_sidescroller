# file to handle util stuff


def create_array(w,h):
    #creates a 2 dimensional array with w-idth and h-eight
    array = []
    row = [0] * h
    for i in range(w):
        array.append(row.copy())
    return array
