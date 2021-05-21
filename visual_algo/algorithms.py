import time

def bubbleSort(array, drawArray, speed):
    length = len(array)
  
    for i in range(length-1):
        for j in range(0, length-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
                drawArray(array, ['white' if x == j or x == j+1 else 'blue' for x in range(len(array))])
                time.sleep(speed)
