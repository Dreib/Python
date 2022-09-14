players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

sum = 0
sum2 = 0

for i in players:
    sum += i

mean = sum/len(players)

for j in players:
    sum2 += (j-mean)**2

v = sum2/len(players)

std = v**0.5

f = int(mean-std)
t = int(mean+std)

count = 0

for x in players:
    if x in range(f, t):
        count += 1

print(count)