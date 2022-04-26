import random

number_N = 1000000
sigma_N = 0
for x in range(number_N):
    sigma_U = 0
    n = 0
    while sigma_U < 1:
        sigma_U = sigma_U + random.uniform(0,1)
        n = n + 1
    sigma_N = sigma_N + n
print(sigma_N/number_N)