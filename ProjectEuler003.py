#Project Euler, Problem 3
#Largest prime factor

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import time

def largestprimefactor(N):
    """This function will return the largest prime factor of a given number N."""
    i, n = 2, N
    while i * i < n:
        while n % i == 0:
            n = n/i
        i = i+1
    return int(n)

start = time.time()
print(largestprimefactor(600851475143))
print(time.time() - start)
#6857 in 0.0 secs