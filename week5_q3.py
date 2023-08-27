firstprime = 0

for num in L:
    if num > 1:
        isprime = True
        for i in range(2,num):
            if num % i == 0:
                isprime = False
                break
        if isprime:
            firstprime = num
            break

print(firstprime,end = ""
