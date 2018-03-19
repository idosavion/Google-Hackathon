import Board, Output


def getMissions(rows):
    missions = []
    for i in rows[1:]:
        missions.append(i.split())
    return missions


def parse_params(param):
    broke = param.split()
    return broke


def file_parse(input_file):
    # parse the first line
    file = open(input_file, 'r')
    rows = file.readlines()
    params = parse_params(rows[0])
    return params, getMissions(rows)


def create_schedule(params, missions):
    board = Board.Board(params[0], params[1], params[2], params[3], params[4], params[5], missions)
    board.assign_rides()
    Output.writeOuput("a_example.out", board)


params, missions = file_parse('a_example.in')
create_schedule(params, missions)
