# Selection Sort Algorithm
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
    for i in range(1, len(inputArray)): 
        key = inputArray[i] 
        j = i-1
        while j >=0 and key < inputArray[j] : 
                inputArray[j+1] = inputArray[j] 
                j -= 1
        inputArray[j+1] = key 
    
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