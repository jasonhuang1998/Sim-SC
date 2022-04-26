import math
import random

round1 = 100
ans = 0
for i in range(round1):
    r = 100000
    s = 0
    for y in range(r):
        x = random.uniform(-2,2)
        s = s + math.exp(x + x * x)
    ans  = ans + s/r*4
    #print(s/r*4)
print(ans / round1)