def fishcount(values):
    for i in range(0, len(values)):
        values[i] = int(values[i])
    for i in range(256):
        for i in range(0, len(values)):
            if values[i] == 0:
                values[i] = 6
                values.append(8)
            else:
                values[i] -= 1
    return len(values)


new_vals = [i.split(",") for i in open('input.txt', 'r')]
new_vals = new_vals[0]
final_val = fishcount(new_vals)

print(final_val)
