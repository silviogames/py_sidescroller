# file to handle util stuff
import random 

def create_array(w,h):
    #creates a 2 dimensional array with w-idth and h-eight
    array = []
    row = [0] * h
    for i in range(w):
        array.append(row.copy())
    return array

def random_range(*pair):
    #creates a weighted table for random number generation
    rnd_set = []
    for vp in pair:
       value, num = vp
       for i in range(num):
           rnd_set.append(value)
    return rnd_set[random.randint(0,len(rnd_set)-1)] 
        
        
