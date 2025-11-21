# This is the 6th day of 100 problems to solve before 31st of dec 2025 
# This problem is an elaboration of if statements 
# '''Given an integer n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20 print Weird
# If n is even and greater than 20, print Not Weird '''
 
# import math
# import os
# import random
# import re
# import sys



# if __name__ == '__main__':
#     n = int(input().strip())
#     if n == 2 > n <5:
#         print("Not Weird")
#     elif 6 > n < 20:
#         print("Weird")
#     else:
#         print("Not Weird")    
    
# # if n/2 == 0:
#     # print("n is even")
# # else:
#     # print("n is odd")
 
#!/bin/python3
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n == 2 > n <5:
        print("Not Weird")
    elif 6 > n < 20:
        print("Weird")
    else:
        print("Not Weird")   
    if n/2 == 0:
        print("Weird")
    
    #Correct answer 
    '''n = int(input().strip())

if n % 2 != 0:          # odd numbers
    print("Weird")
else:                   # even numbers
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:               # n > 20
        print("Not Weird")
'''