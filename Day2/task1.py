hp = 0
depth = 0
instructions = [i.split(" ") for i in open("day2input.txt", "r")]

for i in range(0, len(instructions)):
    if str(instructions[i][0]) == "forward":
        hp += int(instructions[i][1])
    elif str(instructions[i][0]) == "up":
        depth -= int(instructions[i][1])
    elif str(instructions[i][0]) == "down":
        depth += int(instructions[i][1])
    else:
        continue

# depth += sum([-int(instructions[i][1]) if str(instructions[i][0]) == "down" and
#                                               str(instructions[i][0]) != "forward" else int(instructions[i][1])])
# car = [int(i) for i in instructions[i][i + 1] if instructions[i] == "forward"]


print(f"{hp * depth}")
