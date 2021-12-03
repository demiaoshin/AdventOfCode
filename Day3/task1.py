# calculate gamma rate as the most significant bit of each column
# calculate epsilon rate as the most significant bit of each column
# you only have to calculate gamma rate in a for loop (just reverse the answer for epsilon rate

def calculate_rates(values):
    gamma_rate = ""
    gamma_column = []
    epsilon_rate = ""
    for i in range(len(values[0])-1):
        for value in values:
            gamma_column.append(value[i])
        if gamma_column.count("1") > gamma_column.count("0"):
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
        gamma_column = []
    den_gamma_rate = int(gamma_rate, 2)
    den_epsilon_rate = int(epsilon_rate, 2)
    return den_epsilon_rate * den_gamma_rate


binvals = [str(i) for i in open('day3input.txt', 'r')]
print(calculate_rates(binvals))

