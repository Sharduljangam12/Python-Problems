#This is the 3rd day of 100 problems before 31st dec 2025 
#This program will find the that the given number is prime or not
# For example, 
# to check if 29 is prime, find its square root: \(\sqrt{29}\approx 5.38\). 
#  The prime numbers to check are 2, 3, and 5.
#  Divide 29 by each of these: \(29\div 2\) is not a whole number, \(29\div 3\) is not a whole number, and \(29\div 5\) is not a whole number.  Determine primality: If the number is not divisible by any of the primes you tested, it is a prime number. If it is divisible by any of them, it is not prime.
import math
# divisor_list = [2, 3, 5 ]
# results_list = []

# for num in divisor_list:
#     results = num/x
#     results_list.append(results)

x = int(input("Enter a number you want to check is prime or not :"))

d1 = 2
d2 = 3
d3 = 5

if x % d1 == 0 or x % d2 == 0 or x % d3 == 0:
    print(f" Number {x} is not prime ")
else:
    print(f"Number {x} is Prime ")