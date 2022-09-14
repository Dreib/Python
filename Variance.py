vac_nums = [0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1,
            2, 2, 2, 2,
            3, 3, 3
            ]

sum = 0

for i in vac_nums:
    sum += i

mean = sum / len(vac_nums)

sum2 = 0

for j in vac_nums:
    sum2 += (j - mean) ** 2

v = sum2 / len(vac_nums)

print(v)