'''
Mixed Series:

Problem

Odd positions → Fibonacci
Even positions → Prime numbers

Series
1, 2, 1, 3, 2, 5, 3, 7...

Find the Nth term.

'''

def fibonacci(n):
    a,b = 1,1
    for i in range (n-1):
        a,b = b, a+b
    return a

def prime(n):
    count = 0
    num = 2
    while True:
        for i in range (2, num):
            if num%1 == 0:
                break
        else:
            count += 1
            if count == n:
                return num 
            num += 1
            
n = int(input())
if n%2 == 1:
    print(fibonacci((n//2)+1))
else:
    print(prime(n//2))