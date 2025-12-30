#move all zeros in an array to end ?

def move_zeros_to_end(arr):
    result=[]
    count=0  # WE WILL COUNT THE ZEROS 

    for num in arr:
        if num!=0:
            result.append(num)  # SEPERATING THE ZEROS FROM AN ARRAY
        else:
            count +=1   # COUNING ZEROS
    result.extend([0]* count)  # ADDING COUNTED ZEROS TO THE END OF THE ARRAY 
    return result  # KEEPING THE RESULT VALUES 

arr1=[1,2,3,0,0,6]
print("original array ",arr1)
print("modified array", move_zeros_to_end(arr1) )