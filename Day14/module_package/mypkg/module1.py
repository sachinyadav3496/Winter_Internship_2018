def pat1(n):
    for var in range(n) : 
        print("*"*var)

def pat2(n) : 
    for var in range(n) : 
        print("*"*(n-var))

def pat3(n) : 
    for var in range(n) : 
        print(" "*var,end='')
        print("*"*(n-var))

def pat4(n) : 
    for var in range(n) : 
        print(" "*(n-var),end='')
        print("*"*var)

def even(n):
    if n % 2 : 
        return False
    return True

def odd(n) : 
    if n % 2 : 
        return True 
    return False

def prime(n) : 
    for var in range(2,n//2+1) : 
        if n % var == 0 : 
            return False
    return True 

def palindrome(n) : 
    temp = n 
    r = 0
    while n : 
        d  = n % 10 #last digin 
        r = r*10 + d 
        n = n // 10 
    if temp == r : 
        return True 
    return False 

def armstrong(n) : 
    temp = n 
    p = 0 
    while n : 
        p = p + 1
        n = n // 10
    n = temp 
    r = 0 
    while n : 
        d = n % 10 
        r = r + d ** p 
        n = n // 10 
    if r == temp : 
        return True 
    return False
