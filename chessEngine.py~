#!/usr/bin/env python
# Chess engine
# Amol Dharmadhikari <adharma@cs.usfca.edu>

import string, sys
from chesscommons import *
    
# Interface for Player classes
class AbstractPlayer:
    def __init__(self, name):
	    self.name = name

    # This method will return a move
    # whoseMove -> 'white' or 'black'
    # board -> the Board object
    def getMove(self, board, whoseMove):
	    pass

    # Returns true/false depending on whether the move is legal or not
    # in the context of the board and whoseMove
    def isLegal(self, board, whoseMove):
	    pass

    def getName(self):
	    return self.name

# class HumanPlayer
class HumanPlayer(AbstractPlayer):
    def __init__(self):
	    AbstractPlayer.__init__(self, 'HUMAN')
    
    # Read the move from the console, perform error checking i.e. 
    # ensure that the move made is that of the color who is supposed
    # to make it and is a legal move and return it. 
    def getMove(self, board, whoseMove):
	    ret = raw_input('Enter move: ')
	    while 1:
	        if self.isLegal(ret, board, whoseMove):
		        break
	        ret = raw_input('Enter move: ')

	    return ret

    # Check whether the move is legal in the context of the board
    # and whoseMove
    # Returning true for now
    def isLegal(self, move, board, whoseMove):
	    return 1

    def getName(self):
	    return AbstractPlayer.getName(self)

# class MachinePlayer
class MachinePlayer(AbstractPlayer):
    def __init__(self):
	    AbstractPlayer.__init__(self, 'MACHINE')
    
    # Make the move based on computations for the MachinePlayer
    def getMove(self, board, whoseMove):
	    return self.getRandomLegalMove(board, whoseMove)

    # No need for this method here since its the computer's move. 
    # So simply returning true
    def isLegal(self, board, whoseMove):
	    return 1

    def getName(self):
	    return AbstractPlayer.getName(self)

    def getRandomLegalMove(self, board, whoseMove):
	    pass

# class ChessEngine
class ChessEngine:
    PROMPT1 = 'White Player: Human/Machine: '  
    PROMPT2 = 'Black Player: Human/Machine: ' 
    PLAYERS = ['H', 'M', 'h', 'm']
    HUMANS = ['H', 'h']
    MACHINES = ['M', 'm']

    def __init__(self):
	    # Get an instance of the board
	    self.b = Board()
	    self.b.setStartingPosition()

	    # The white and black players
	    self.whitePlayer = None
	    self.blackPlayer = None

        # Whose move
        self.whoseMove = WHITE_MOVE

        # The current move
        self.move = ''

    # Init game parameters
    def initGameParameters(self):
	    ret1 = raw_input(self.PROMPT1)
	    while 1:
	        if ret1 in self.PLAYERS:
		        break
	        ret1 = raw_input(self.PROMPT1)

	    ret2 = raw_input(self.PROMPT2)
	    while 1:
	        if ret2 in self.PLAYERS:
		        break
	        ret2 = raw_input(self.PROMPT2)

	    self.setPlayers(ret1, ret2)

    def setPlayers(self, white, black):
	    if white in self.HUMANS:
	        self.whitePlayer = HumanPlayer()
	    elif white in self.MACHINES:
	        self.whitePlayer = MachinePlayer()

	    if black in self.HUMANS:
	        self.blackPlayer = HumanPlayer()
	    elif black in self.MACHINES:
	        self.blackPlayer = MachinePlayer()

    # Print the board
    def printBoard(self):
	    print ("White: ", self.whitePlayer.getName())
	    print str(self.b)
	    print ("Black: ", self.blackPlayer.getName())

    # Main loop in which the game is played
    def play(self):
	    while 1:
            self.printBoard()

            try:
                # Get the move from the player whose move it is. Start with
                # white and then alternate
                move = ''
                if self.whoseMove == WHITE_MOVE:
                    move = self.whitePlayer.getMove(self.b, self.whoseMove)
                elif self.whoseMove == BLACK_MOVE:
                    move = self.blackPlayer.getMove(self.b, self.whoseMove)

                # Get new position of the board based on the move
                self.b.newPosition(whoseMove, move)

                # Change whoseMove
                self.whoseMove ^= 1
                
            except IllegalMoveException, e:
                print "Illegal move! Try again"

# Main method
def main(argv):
    chessEngine = ChessEngine()
    chessEngine.initGameParameters()
    chessEngine.play()
    sys.exit(0)

# Entry point	
if __name__ == '__main__':
    main(sys.argv)
