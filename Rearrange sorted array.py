# Python program for the above approach

# Function to print the array
def printArray(arr, n):
for i in range(N):
	print(arr[i],end=" ")
print("\n")


# Function to rearrange the array such
# that odd indexed elements come before
# even indexed elements
def rearrange(arr, N):

#Reduces the size of array by one
#because last element does not need
#to be changed in case N = odd
if (N & 1):
	N-=1

# Initialize the variables
odd_idx = 1
even_idx = 0
max_elem = arr[N - 1] + 1

# Iterate over the range
for i in range(N//2):

	# Add the modified element at
	# the odd position
	arr[i] += (arr[odd_idx] % max_elem) * max_elem
	odd_idx += 2


# Iterate over the range
for i in range(N//2,N):

	# Add the modified element at
	# the even position
	arr[i] += (arr[even_idx] % max_elem) * max_elem
	even_idx += 2


# Iterate over the range
for i in range(N):

	# Divide by the maximum element
	arr[i] = arr[i] // max_elem




# Driver Code
if __name__=="__main__":

arr = [ 1, 2, 3, 4, 5, 16, 18, 19 ]
N = len(arr)

rearrange(arr, N)
printArray(arr, N);


