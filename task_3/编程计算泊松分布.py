import math

def poisson_probability(x, lam=7):
    # 计算泊松分布的累积概率P(X <= x)
    cumulative_prob = sum((lam**k * math.exp(-lam) / math.factorial(k)) for k in range(x+1))
    return cumulative_prob

# 测试
x = int(input())

print(f"{poisson_probability(x):.2f}")