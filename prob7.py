import numpy as np

def next_prime(p_list):
    if len(p_list) == 0:
        return 2
    x = max(p_list) + 2
    while True:
        if np.array([x % p != 0 for p in p_list]).all():
            return x
        x += 2

def update_plist(p_list):
    p_list.append(next_prime(p_list))


p_list = [2, 3]
while len(p_list) < 10000:
    update_plist(p_list)
    l = len(p_list)
    if l % 100 == 0:
        print(l)

print(len(p_list))
print(next_prime(p_list))
