count = 0
values = [int(i) for i in open('day1input.txt', 'r')]

for i in range(0, len(values)-1):
    if i == 0:
        continue
    elif i == len(values)-3:
        if values[-1] > values[i]:
            count += 1
        break
    else:
        if values[i+3] > values[i]:
            count += 1

print(count)