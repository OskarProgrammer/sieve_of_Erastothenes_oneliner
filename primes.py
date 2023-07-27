from functools import reduce


primes = lambda n : (reduce(lambda l, x: l - set(range(x**2,n,x)) # removing multiples of the current x \ 
                if x in l else l # if current x in l remove multiples otherwise return l because there is no more job to do\
                ,range(int(n ** 0.5) + 1), # sequence of the reduce is to the square root of n\
                set(range(2,n)))) # creating starting set of numbers from 2 to n

print(primes(10))