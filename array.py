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
    if len(inputArray) > 1:
        # Finding the mid of the array
        mid = len(inputArray)//2
        # Dividing the array elements
        L = inputArray[:mid]
        # into 2 halves
        R = inputArray[mid:]
        # Sorting the first half
        sortElements(L)
        # Sorting the second half
        sortElements(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                inputArray[k] = L[i]
                i += 1
            else:
                inputArray[k] = R[j]
                j += 1
                k += 1
        # Checking if any element was left
        while i < len(L):
            inputArray[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            inputArray[k] = R[j]
            j += 1
            k += 1
    
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
    sequence = [i for i in range(input_size)] 
    start = time.time() # start timer   
    result = MinMidMax(sequence)
    print(result)
    print("Input size=", input_size, " Time taken=", time.time()-start)  
	
 
if __name__ == '__main__':
    k = 1000
    measure_time(2*k)  
    # measure_time(10*k)  
    # measure_time(50*k)  
    # measure_time(200*k)  
    # measure_time(1000*k)  