h1 = ((int(input())) * 60) * 60
m1 = ((int(input())) * 60)
s1 = int(input())
h2 = ((int(input())) * 60) * 60
m2 = ((int(input())) * 60)
s2 = int(input())

walk_time = h1 + m1 + s1
rain_time = h2 + m2 + s2

print(rain_time - walk_time)
