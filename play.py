from tictactoe import TicTacToe
from network import Agent
from player import Player
import pickle

# player against ai
def play(player0, player1):
    
    TicTacToe(printing=True)

    # play game
    # while game.winner == -1:
    #     if game.player == 0:
    #         winner = game.play(player0.get_input())
    #     else:
    #         winner = game.play(player1.get_input(board=game.board))
    # return winner

if __name__ == '__main__':
    agent = Agent.load(f'players/test1')
    player0 = Player()
    player1 = Player(agent=agent)

    play(player0, player1)