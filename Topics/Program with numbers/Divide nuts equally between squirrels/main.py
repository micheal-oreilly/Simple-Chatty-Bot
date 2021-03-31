n = int(input())
k = int(input())

remainder = k % n
nuts = int((k - remainder) / n)
print(nuts)
