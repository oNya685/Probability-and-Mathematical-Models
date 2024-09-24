import random

MAX_TIMES = 100000

coin_a = 0
coin_b = 0

for n in range(MAX_TIMES):
    coin = random.randint(0, 1)
    if(coin == 0):
        coin_a += 1

print(f"{coin_a/MAX_TIMES:.2f}")