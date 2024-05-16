# Open the file in read mode
file= open("numbers.txt", 'r') 
# Create an empty list to store the numbers
num_list = []
# Loop through each line in the file
for num in file:
        #strip() method removes any whitespaces
        number = int(num.strip())
        # Append the number to the list
        num_list.append(number)
print(num_list)
#[3, 114, 20, 630, 21, 735, 16, 4949, 27, 4823, 28, 33, 1243, 19, 27, 457, 34, 2054, 29, 2, 973, 8, 949, 31, 45]

#To sort this num_list
sorted_num_list=[]
while len(num_list)>0:  #To repeat the steps upto complete the num_list.
    minimum=num_list[0] #Find the minimum numbers in num_list.
    for x in num_list:
        if x<minimum:
            minimum=x
#To Add the minimum element in order to the sorted_num_list.            
    sorted_num_list.append(minimum)
#To remove the minimum elements in order from num_list.    
    num_list.remove(minimum)    
print (sorted_num_list)

#create a new file (sorted.txt) and store the sorted numbers in it line by line.
#f=open("sorted.txt", 'x') #"x"- will create a file
f= open("sorted.txt", 'w')
for x in sorted_num_list:
    f.write(str(x)+ "\n") 
f.close()

