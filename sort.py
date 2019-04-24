# import modules
import time # to measure the running time of sorting algorithm
import random # to genearte random input instances for the sorting algorithm


# the code below defines a function that will create an array of random number, n being the number of values required in the array
def random_array(n):
    array = []
    for i in range(0,n,1):
        array.append(random.randint(0, 100)) # added "random.randint" to code on project sheet
    return array

# the code below defines a function for bubbleSort
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


# adapted from https://www.sanfoundry.com/python-program-implement-bucket-sort/
def bucketSort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length):
        insertion_sorta(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sorta(alist): # using a different insertion sort algorithm here
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp
 
def selectionSort(alist):   
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
                
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
            
        alist[position]=currentvalue


sorts = [bubbleSort,mergeSort,bucketSort,selectionSort,insertionSort]
input_size = [100,250,500,750,1000,1250,2500,3750,5000,6250,7500,8750,10000]
num_runs = 10
results = []

t = open("results.csv", "a+") # code sourced from https://stackoverflow.com/questions/42236689/how-to-write-a-while-loop-into-a-csv-file
t.write("Sort")
t.write(",")
t.write("InputSize")
t.write(",")
t.write("AverageRunningTime")
t.write("\n") # write a new row to the csv file

for i in sorts:
    print(str(i.__name__)) # name of function taken from https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function-without-using-traceback
    for j in input_size:
        for r in range(num_runs):
            start_time = time.time()
            i(random_array(j))
            end_time = time.time()
            time_elapsed = round((end_time - start_time)*1000,3) # calculate running time and convert to milliseconds and 3 decimals of places
            results.append(time_elapsed)
        print(results)
        print(sum(results)/len(results))
        t.write(str(i.__name__)) # writes the text 'BubbleSort' to the first cell in the csv file
        t.write(",") # creates a new column in the csv file
        t.write(str(j)) # writes the text '100 ' to the first cell in the csv file
        t.write(",") # creates a new column in the csv file
        t.write(str(sum(results)/len(results))) # convert time_elapsed to sting as write will note read a float and write to csv file
        t.write("\n") # write a new row to the csv file
        results = []

t.close()
