game_board = []
final_num = 0


def checkys(board):
    potv = []
    for row in board:
        if row.count("Y") == 5:
            return True
        else:
            for i in range(5):
                if row[i] == "Y":
                    potv.append(i)
            if len(potv) > 4:
                for i in range(5):
                    if potv.count(i) == 5:
                        return True
                    else:
                        continue
    return False


def bingo(bingonums, gameboards):
    global final_num
    boards = []
    for i in range(0, len(gameboards), 5):
        boards.append((gameboards[i:i + 5]))
    for number in bingonums:
        for board in boards:
            if len(boards) == 1:
                final_num = int(number)
                return boards[0]
            for row in board:
                if number in row:
                    row[row.index(number)] = "Y"
            else:
                if checkys(board):
                    boards.remove(board)


def calculate_result(board):
    total = 0
    for row in board:
        for num in row:
            if num == "Y":
                continue
            else:
                total += int(num)
    total = total * final_num
    return total


with open('task1testinput.txt', 'r') as f:
    values = f.readline()
    values = values[:-1]  # get rid of \n
    values = values.split(",")
    game_boards = [i.split() for i in f if i != "\n"]
    final_board = bingo(values, game_boards)
    print(final_board)
    result = calculate_result(final_board)
    print(result)

