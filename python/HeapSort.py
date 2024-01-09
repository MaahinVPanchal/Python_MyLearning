def heapify(arr, n, i): 
	largest = i 
	left = 2 * i + 1 
	right = 2 * i + 2 

	if left < n and arr[i] < arr[left]:
		largest = left

	if right < n and arr[largest] < arr[right]:
		largest = right

	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i]) 

		heapify(arr, n, largest)

def HeapSort(arr):
	n = len(arr)

	for i in range(n // 2 - 1, -1, -1): 
		heapify(arr, n, i)

	for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i])
		heapify(arr, i, 0)

arr = [70,40,50,20,30,10,60,90,80,100,] 
HeapSort(arr) 
n = len(arr) 
print('We get Sorted array as') 
for i in range(n):   
	print(arr[i])