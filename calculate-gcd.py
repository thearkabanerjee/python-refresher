a = int(input())
b = int(input())

factors = []

for i in range (1, a+1):
    for j in range (1, b+1):
        if (a % i == 0):
            if (b % j == 0):
                if (i == j):
                    factors.append(i)

print (factors[-1])
