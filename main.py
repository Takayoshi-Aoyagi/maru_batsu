import itertools

import numpy as np

MARU = "O"
BATSU = "X"

def get_permutations():
    data = itertools.permutations(range(9))
    return data

def to_game_data(permutation):
    #data = {}
    data = []
    for idx, cell_no in enumerate(permutation):
        mb = MARU if idx % 2 == 0 else BATSU
        data.append((idx, cell_no, mb))
        #data[cell_no] = (idx, mb)
    return data
    
def print_board(game_data):
    print game_data
    print "+-----+-----+-----+"
    print "| {0}:{1} | {2}:{3} | {4}:{5} |".format(game_data[0][1], game_data[0][2], game_data[1][1], game_data[1][2], game_data[2][1], game_data[2][2])
    print "+-----+-----+-----+"
    print "| {0}:{1} | {2}:{3} | {4}:{5} |".format(game_data[3][1], game_data[3][2], game_data[4][1], game_data[4][2], game_data[5][1], game_data[5][2])
    print "+-----+-----+-----+"
    print "| {0}:{1} | {2}:{3} | {4}:{5} |".format(game_data[6][1], game_data[6][2], game_data[7][1], game_data[7][2], game_data[8][1], game_data[8][2])
    print "+-----+-----+-----+"

def to_judged_data(game_data):
    winner = MARU
    arr = np.array(game_data)
    matrix = np.reshape(arr, (3, 3, 3))
    print matrix
    return (game_data, winner)
    
def execute():
    for permutation in  get_permutations():
        game_data = to_game_data(permutation)
        judged_data = to_judged_data(game_data)
        print_board(judged_data[0])

if __name__ == '__main__':
    execute()
         
