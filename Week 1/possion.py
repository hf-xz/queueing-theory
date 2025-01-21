import math

l = 3
i = 5

p = math.exp(-l)

for i in range(1, i+1):
    p = p * l / i

print(p)
