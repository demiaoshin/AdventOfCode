
count = 0
values = [int(i) for i in open('day1input.txt', 'r')]

for i in range(0, len(values)-1):
    if i == 0:
        continue
    else:
        if values[i] > values[i-1]:
            count += 1

print(count)