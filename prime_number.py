def is_prime_number(n: int):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

sum = 2

n = input()

for i in range(3, int(n)+1):
    if is_prime_number(i): sum+=i
    elif i % 2 == 0: sum+=i

print(sum)
