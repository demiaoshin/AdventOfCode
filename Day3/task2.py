# calculating oxygen generator rating and CO2 scrubber rating
oxyg_prate = []
oxy_column = []
co_column = []
co_prate = []


def firstcheck(values):
    global oxyg_prate, co_column, oxy_column, co_prate
    for value in values:
        oxy_column.append(value[0])
    if oxy_column.count("1") > oxy_column.count("0"):
        oxyg_prate = [value for value in values if value[0] == "1"]
        co_prate = [value for value in values if value[0] == "0"]
    elif oxy_column.count("1") == oxy_column.count("0"):
        oxyg_prate = [value for value in values if value[0] == "1"]
        co_prate = [value for value in values if value[0] == "0"]
    else:
        oxyg_prate = [value for value in values if value[0] == "0"]
        co_prate = [value for value in values if value[0] == "1"]
    oxy_column = []
    co_column = []


def calculate_rates(values):
    global oxyg_prate, co_column, oxy_column, co_prate
    firstcheck(values)
    for i in range(1, len(values[0])-1):
        for value in values:
            if value in oxyg_prate:
                oxy_column.append(value[i])
            elif value in co_prate:
                co_column.append(value[i])
            else:
                continue
        if oxy_column.count("1") > oxy_column.count("0"):
            oxyg_prate = [value for value in oxyg_prate if value[i] == "1"]
        elif oxy_column.count("1") == oxy_column.count("0"):
            oxyg_prate = [value for value in oxyg_prate if value[i] == "1"]
        else:
            oxyg_prate = [value for value in oxyg_prate if value[i] == "0"]
        if len(co_prate) == 1:
            break
        if co_column.count("1") > co_column.count("0"):
            co_prate = [value for value in co_prate if value[i] == "0"]
        elif co_column.count("1") == co_column.count("0"):
            co_prate = [value for value in co_prate if value[i] == "0"]
        else:
            co_prate = [value for value in co_prate if value[i] == "1"]
        oxy_column = []
        co_column = []
    den_oxyg_rate = int(oxyg_prate[-1], 2)
    den_co_rate = int(co_prate[-1], 2)
    return den_oxyg_rate * den_co_rate


binvals = [str(i) for i in open('day3input.txt', 'r')]
print(calculate_rates(binvals))
