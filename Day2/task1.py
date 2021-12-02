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


print(f"{hp * depth}")
