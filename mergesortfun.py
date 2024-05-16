'''
Objective: To merge sort a given unsorted array.
First need to find the mid index of array.
    mid=len(arr)//2
By using this mid index, split the given array into two parts.
    left_arr=arr[:mid+1]
    right_arr=arr[mid+1:]
Now, we have two unsorted arrays, need to sorted them.
Recursively call the merge_sort function to sort both arrays.
    sorted_left=merge_sort(left_arr)
    sorted_right=merge_sort(right_arr)
This recursion will continues upto the length of array become 1 or 0.
If the length of array is 0 or 1, then the array is return as it is.
    If len(arr)<=1:
        return arr
Now, merge this two sorted arrays using merge function, convert into single sorted array.
    return merge(sorted_left,sorted_right)
Compare the values in both arrays and the minimum values moved to the new empty array.

'''

def merge_sort(arr):
    if len(arr)<=1: #If the length of array is 0 or 1, then the array is return as it is
        return arr
    mid=len(arr)//2 #to find mid index or array.
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    print(left_arr)
    print(right_arr)
#we have two unsorted arrays, need to sorted them
    sorted_left=merge_sort(left_arr)
    sorted_right=merge_sort(right_arr)
    print(sorted_left)
    print(sorted_right)
#merge this two sorted arrays using merge function
    return merge(sorted_left,sorted_right)
def merge(sorted_left,sorted_right):

    arr1 = []   #create empty array to store the sorted array
    i=0   # index of left array
    j=0   # index of right array
    while i<len(sorted_left) and j<len(sorted_right):
        if sorted_left[i]<sorted_right[j]:
            arr1.append(sorted_left[i])
            i+=1
        else:
            arr1.append(sorted_right[j])
            j+=1
    while i < len(sorted_left):
        arr1.append(sorted_left[i])
        i+=1 
    while j < len(sorted_right):
        arr1.append(sorted_right[j])
        j+=1        
    return arr1

arr=[10,6,2,4,8,5,3,1]
sorted_array=merge_sort(arr)
print("sorted arr",sorted_array)

