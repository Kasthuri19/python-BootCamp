'''
2,4,6,1,3,5
F     S       2>1=F>S, So replace the 1 to the Fth position. remaining elements right shift.
              Now the F and S both to be moved to next index.
1,2,4,6,3,5 
  F     S     2<3=F<S, There is no changes in elements.
              F only moved to next index.
1,2,4,6,3,5
    F   S     4>3=F>S,  So replace 3 to the Fth position. Remaining elements right shift.
              Now the F and S both to be moved to next index.
1,2,3,4,6,5
      F   S   4<5=F<S, There is no changes in elements.
              F only moved to next index.
1,2,3,4,6,5
        F S   6>5=F>5, So replace the 5 to the Fth position. remaining elements right shift.
              S reached end index,so no need to move next. F only moved to next. Both reaches end index. 
1,2,3,4,5,6   - The array is sorted.

1,1,1,3,3,3
F     S
  F   S
    F S
      F
      S
Pseudocode:-
Objective: Write a function to merge both sub-arrays using in-place method.
First we need to know that the start pointer of both sub arrays.
   The start pointer of first subarray is first 
   The start pointer of second subarray is second 
   Last index of combined array = end
Compare the first and second position elements:
    If the F is greater than S, then move S to the F position.
        Remaining elements right shift upto the S position.
    if arr[F]>arr[S]:
        min_value=arr[S]  minimum value(S) is stored in min_value varaible.
        Right shift the elements from S to F.
        arr[S]=arr[S-1]
        arr[S-1]=arr[S-2]
        ...
        Now arr[F]=min_value.
        F+=1,S+=1
    If the F is less than S, then there is no changes in elements in array.
        F only moved to next position.
    if arr[F]<arr[S]:
      F+=1
This steps are continue upto second will reach the end of the array. Or when the first is reached second.
 
'''

def mergeInplace_recursion(arr, first, second, end):
    if first>=second or second>end:     #while first<second and second<=end:
        return arr
    
    if arr[first]>arr[second]:
        min_value=arr[second]
       
        s=second
        
        while s>first:
            arr[s]=arr[s-1]
            s=s-1
        arr[first]=min_value   
        
        mergeInplace(arr, first+1, second+1, end) #function call
    else:
        mergeInplace(arr, first+1, second, end)
    
    return arr

def mergeInplace(arr,first,second,end):
    while first<second and second<=end:
        if arr[first]>arr[second]:
            min_value=arr[second]
       
            s=second
        
            while s>first:
                arr[s]=arr[s-1]
                s=s-1
            arr[first]=min_value 
            first+=1
            second+=1 
        else:
            first+=1
    return arr

arr = [2,4,6,1,3,5]
mergeInplace(arr, 0, 3, len(arr)-1) #main function call
print(arr)



        

    