import math

d = str(input("Введите число d: "))
print(math.pi)
d_len = len(d.split('.')[1])

i = 0
num_pi = str(math.pi)
while i < (d_len + 2) and i < len(num_pi):
    print(num_pi[i], end="")
    i += 1