# Write code for algorithm 2 below
#2. Write a function that prints the natural numbers from 1 to n.

def natural(n):
    if n == 1 :
        print(n)
        #can either be print(1) as well

    else:
        natural(n-1)
        print(n)

natural(5)