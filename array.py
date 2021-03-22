# Bubble Sort Algorithm
import time 
def MinMidMax(inputArray):
    return Min(inputArray),median(inputArray),Max(inputArray)

def Min(inputArray):
    min = inputArray[0]
    for i in range(1,len(inputArray)):
        if min > inputArray[i]:
            min = inputArray[i]
    return min

def Max(inputArray):
    max = inputArray[0]
    for i in range(1,len(inputArray)):
        if max < inputArray[i]:
            max = inputArray[i]
    return max

def sortElements(inputArray):
    for i in range(0, len(inputArray)):
        for j in range(i+1,len(inputArray)):
            if inputArray[i] > inputArray[j]:
                k = inputArray[i]
                inputArray[i] = inputArray[j]
                inputArray[j] = k
    
def median(inputArray):
    sortElements(inputArray)
    med = 0
    n= len(inputArray)
    if n % 2 == 0:
        med = (inputArray[int(n/2)]+inputArray[int((n/2)-1)])/2
    else:
        med = inputArray[int((n-1)/2)]     
    return med   


def measure_time(input_size):  
    sequence = [i for i in range(input_size)] # input = a list [0,1,2,...]  
    # print(sequence)  
    start = time.time() # start timer  
    # (min(sequence)) # execute the function with the sequence  
    # (MinMidMax(sequence)) # execute the function with the sequence  
    result = MinMidMax(sequence)
    print(result)
    print("Input size=", input_size, " Time taken=", time.time()-start)  
	
 
if __name__ == '__main__':
    k = 1000
    # measure_time(2*k)  
    # measure_time(10*k)  
    # measure_time(50*k)  
    measure_time(200*k)  
    # measure_time(1000*k)  