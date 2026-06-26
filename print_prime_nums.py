# i kindda forgot how to print prime numbers
# gotta try writing the code for it

a = int(input())

for i in range(1, a+1):
    factors = 0
    for j in range (1, i+1):
        if (i % j == 0):
            factors += 1
    if (factors == 2):
        print (i, end = ' ')