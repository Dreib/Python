n = int(input())

for x in range(1, n):
    if not x % 2 == 0:
        if x % 3 == 0 and x % 5 == 0:
            print("SoloLearn")
        elif x % 3 == 0:
            print("Solo")
        elif x % 5 == 0:
            print("Learn")
        else:
            print(x)
    else:
        continue