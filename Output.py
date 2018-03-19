import Board


def writeOuput(name, board):
    file = open(name, 'w')
    for car in board.get_car_list():
        line = " ".join(str(i) for i in car.getRides())
        line = str(len(car.getRides())) + " " + line + "\n"
        file.write(line)
    file.close()


def writeOuput2(name, board):
    file = open(name, 'w')
    a = [[2], [1, 3], [4]]
    for i in range(len(a)):
        line = " ".join(str(i) for i in a[i])
        line = str(len(a[i])) + " " + line + "\n"
        file.write(line)
    file.close()


writeOuput2("test_output.txt", 0)
