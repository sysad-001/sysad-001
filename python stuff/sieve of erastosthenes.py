from importlib.resources import path
import os
import math

def SieveOfEratosthenes(n):
     
    '''Create a boolean array "prime[0..n]" and initialize
     all entries it as true. A value in prime[i] will
     finally be false if i is Not a prime, else true.'''
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False

    listofprimes=[]
    fd = os.open("primes.txt",os.O_RDWR)
    for p in range(n+1):
        if prime[p]:
            print(p)
            #os.write(fd,str(p).encode())
            os.write(fd,str('■'*p+'\n').encode())
            # os.write(fd,(('■'*(p))+'\n').encode())
       
 
# driver program
if __name__=='__main__':
    n=int(input("to what lengths does one go to? "))
    print ("Following are the prime numbers smaller", end=' ')
    #Use print("Following are the prime numbers smaller") for Python 3
    print ("than or equal to", n)
    #Use print("than or equal to", n) for Python 3
    SieveOfEratosthenes(n)
    input("end me.")
