"""
3,8,9,7,6,4,10,2,1    - Let's take pivot as 6
L       P         R   - 3<6, 6>1  -> L<P, P>R  -> L+=1
3,8,9,7,6,4,10,2,1
  L     P        R    - 8>6, 6>1  -> L>P, P>R  -> Swap L and R  -> L+=1
3,1,9,7,6,4,10,2,8
    L   P        R    - 9>6, 6<8  -> L>P, P<R  -> R-=1
3,1,9,7,6,4,10,2,8
    L   P      R      - 9>6, 6>2  -> L>P, P>R  -> Swap L and R  -> L+=1
3,1,2,7,6,4,10,9,8
      L P      R      - 7>6, 6<9  -> L>P, P<R  -> R-=1
3,1,2,7,6,4,10,9,8
      L P    R        - 7>6, 6<10 -> L>P, P<R  -> R-=1
3,1,2,7,6,4,10,9,8
      L P R           - 7>6, 6>4  -> L>P, P>R  -> Swap L and R  -> L+=1
3,1,2,4,6,7,10,9,8
        L R           - 6=6, 6<7  -> L=P, P <R  -> R-=1
        P
3,1,2,4,6,7,10,9,8
        L             L=P
        R             R=P    No changes
        P  
3,1,2,4   P=1               7,10,9,8
L P   R     L>P, P<R        L P    R
3,1,2,4                     7,10,9,8
L P R       L>P, P<R          L    R   
3,1,2,4                     7,8,9,10
L R      L>P, P=R, L>R,       L    R
  p      So swap
1,3,2,4                     7,8,9,10
1,2,3,4

Psuedocode:
Objective: To quick sort a given array by using pivot value.
Rearrange values before pivot as smaller and values after pivot as larger elements.
Assign arr[len(arr)//2] as pivot.
When left element value is less than the pivot value then there is no changes.
Then left index moved to next element and compare with pivot value.
If the left value is greter than the pivot then swap it with right side element which is smaller than the pivot value.
Right index value should be greater than the pivot value.
If not then swap it with left element.
Continue this process until the array is sorted.
"""
def quicksort(arr,left,right,level):
    # Rearrange values before pivot as smaller and values after pivot as larger elements.
    # Assign arr[len(arr)//2] as pivot.
    print("level",level)
    print("arr",arr[left:right+1])
    if left>=right:      # when the left value is moved next to the right then it is break.
        return  
    p=arr[(left+right)//2]
    i=left
    j=right
    while i<j:
        while arr[i]<p:    #find the first left index that need to be swap. 
           i+=1
        
        while arr[j]>p:  #find the first right index that need to be swap.
            j-=1
        
        arr[i],arr[j]=arr[j],arr[i]  #swap the left and right elements.
        #array after rearranging =[3,1,2,4,6,7,10,9,8]
    print("New",arr[left:right+1])  
    #Store the pivot index to handle the function call left and right  
    pivot_index=i      
    #left array
    quicksort(arr,left,pivot_index-1,level+1)    #secondary function call
    print('back to level',level)
    #right array
    quicksort(arr,pivot_index+1,right,level+1)    #secondary function call
    print("completed level",level)
    return arr
arr=[3,8,9,7,6,4,10,2,1]
quicksort(arr,0,len(arr)-1,0)   #main function call
print("sorted arr",arr)
        
    
