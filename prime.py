def prime(n):
    prime_num = []
    stop = int(input(""))
    for i in range (2 ,stop + 1):
        counter = 0
        for j in range(1, i + 1):
            if i % j == 0:
                counter += 1
        if counter == 2:
            prime_num.append(i)
    print(prime_num)
    return (prime_num[n-1])

print(prime(4))
print(prime(6))
    

