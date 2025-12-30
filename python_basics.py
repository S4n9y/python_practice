# # # # # # # # # # #merging 2 SORTED arrays into an array 

# # # # # # # # # # arr1=[1,2,3,5,7,9]
# # # # # # # # # # arr2=[2,3,4,5,6,7]

# # # # # # # # # # merged=[]
# # # # # # # # # # i=j=0

# # # # # # # # # # while i< len(arr1) and j< len(arr2):
# # # # # # # # # #     if arr1[i] < arr2[j]:
# # # # # # # # # #         merged.append(arr1[i])
# # # # # # # # # #         i +=1
# # # # # # # # # #     elif arr1[i] == arr2[j]:
# # # # # # # # # #         merged.append(arr1[i])
# # # # # # # # # #         merged.append(arr2[j])
# # # # # # # # # #         i += 1
# # # # # # # # # #         j += 2
# # # # # # # # # #     else:
# # # # # # # # # #         merged.append(arr2[j])
# # # # # # # # # #         j+=1

# # # # # # # # # # merged.extend(arr1[i:])
# # # # # # # # # # merged.extend(arr2[j:])

# # # # # # # # # # print(merged)

# # # # # # # # # # find first non-repeating character ? in string

# # # # # # # # # a= input("enter a string: ")

# # # # # # # # # for ch in a:
# # # # # # # # #     if a.count(ch)==1:
# # # # # # # # #         print(" First NON_Repeating character: ",ch)
# # # # # # # # #         break
# # # # # # # # # else:
# # # # # # # # #     print("No , Non-repeating character found ")

# # # # # # # # # # replace all spaces in string with %20

# # # # # # # # # a = input("enter the string :")

# # # # # # # # # R=a.replace(" ",'%20')

# # # # # # # # # print(R)

# # # # # # # # from itertools import permutations

# # # # # # # # a = input("Enter string: ")

# # # # # # # # for p in permutations(a):
# # # # # # # #     print("".join(p))

# # # # # # # #decorators
# # # # # # # # A decorator with nested function
# # # # # # # def decorator(this):
# # # # # # #     def wrapper(a, b):   # wrapper accepts parameters
# # # # # # #         def wrap(woof):   # nested function, expects another function as input
# # # # # # #             woof(a, b)    # call that function with the same (a, b)
# # # # # # #             print("nested line of code of the decorator")

# # # # # # #         print("hi i am sanket using my first line of code.")
# # # # # # #         this(a, b)       # call original function with arguments
# # # # # # #         print("hi i am sanket using my second line of code.")
# # # # # # #         return wrap      # return nested function
# # # # # # #     return wrapper

# # # # # # # @decorator
# # # # # # # def add(a, b):
# # # # # # #     print("this is function to be added in wrapper: ", a + b - 2)

# # # # # # # # Call 'add' — actually runs wrapper
# # # # # # # nested = add(5, 7)

# # # # # # # # Now call the nested function 'wrap' with another function
# # # # # # # def sub(a, b):
# # # # # # #     print("this is function to be added in wrapper:= ", a - b)

# # # # # # # print("--- Now calling nested wrap function ---")
# # # # # # # nested(sub)   # here 'woof' becomes 'sub'

# # # # # # #generator 
# # # # # # def gen():
# # # # # #     print("1st")
# # # # # #     yield 12

# # # # # #     print("2nd")
# # # # # #     yield 13

# # # # # #     print("3rd")
# # # # # #     yield 11

# # # # # # g = gen()

# # # # # # print(next(g))   
# # # # # # print(next(g))  
# # # # # # print(next(g))  


# # # # # #  * Recursion Problems *
# # # # # # Factorial 

# # # # # n = int(input("enter the number: "))
# # # # # def fact(n):
# # # # #     if (n==1 or n==0):
# # # # #         return 1
# # # # #     else:
# # # # #         return n * fact(n-1)
# # # # # print(f" the factorial of {n} is ",fact(n))    

# # # # # def count_fact(n):
# # # # #     count = 0    
# # # # #     for DIGIT in str(fact(n)):   # loop 1 to n
# # # # #         count += 1
# # # # #     return count

# # # # # print("Count is:", count_fact(n))

# # # # # #  Generatee Fibonacci sequence up to n 

# # # # # n = int(input(" enter the number: "))
# # # # # a,b=0,1
# # # # # for i in range(1,n+1):
# # # # #     a,b=b,a+b
# # # # #     print(b,end =" ")

# # # # # TOWER OF HANOI 

# # # # def toh(n, start, aux, end):
# # # #     if n == 1:
# # # #         print(f"Move disk 1 from rod {start} to rod {end}")
# # # #         return
    
# # # #     # Move n-1 disks from start to aux using end as helper
# # # #     toh(n-1, start, end, aux)
    
# # # #     # Move the nth disk from start to end
# # # #     print(f"Move disk {n} from rod {start} to rod {end}")
    
# # # #     # Move the n-1 disks from aux to end using start as helper
# # # #     toh(n-1, aux, start, end)

# # # # # Example with 3 disks
# # # # discs = 3
# # # # toh(discs, "A", "B", "C")

    
    
# # # # find the prime number


# # # n = int(input("Enter the number: "))

# # # if n <= 1:
# # #     print("Not a prime number")
# # # else:
# # #     for i in range(2, n):
# # #         if n % i == 0:
# # #             print("It is not a prime number")
# # #             break
# # #     else:
# # #         print("Prime number")



# # ############### BIT MANIPULATION #############################

# # #check if a number is a power of 2 

# # def is_power_of_2(n):
# #     if n <=0 :
# #         return False
# #     return (n & (n -1))==0

# # n = 22
# # print(is_power_of_2(n))

# #count the number of 1 bits in a number
# def count_ones(n):
#     count = 0
#     while n :
#         n = n &  (n-1)
#         count +=1
#     return count

# n = 15
# print((count_ones(n)))