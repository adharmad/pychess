# common chess data structures and operations
#
# Global constants
WHITE_MOVE = 0
BLACK_MOVE = 1

# class Piece
class Piece:
    NO_PIECE = 0x00000000
    PAWN   = 0x00000001
    BISHOP = 0x00000010
    KNIGHT = 0x00000100
    ROOK   = 0x00001000
    QUEEN  = 0x00010000
    KING   = 0x00100000
    WHITE_MASK = 0x00000000
    BLACK_MASK = 0x10000000
    MAX_BIT_MASK = 0x01111111
	
    # Initialize the piece based on color and piece information passed
    def __init__(self, color='', piece=''):
        self.x = self.NO_PIECE

        if color == 'white' or color == 'WHITE':
            self.x = self.x | self.WHITE_MASK
        elif color == 'black' or color == 'BLACK':
            self.x = self.x | self.BLACK_MASK

        if piece == 'pawn' or piece == 'PAWN':
            self.x = self.x | self.PAWN
        elif piece == 'bishop' or piece == 'BISHOP':
            self.x = self.x | self.BISHOP
        elif piece == 'knight' or piece == 'KNIGHT':
            self.x = self.x | self.KNIGHT
        elif piece == 'rook' or piece == 'ROOK':
            self.x = self.x | self.ROOK
        elif piece == 'queen' or piece == 'QUEEN':
            self.x = self.x | self.QUEEN
        elif piece == 'king' or piece == 'KING':
            self.x = self.x | self.KING

    def isWhite(self):
        return not (self.x & self.WHITE_MASK)

    def isBlack(self):
        return (self.x & self.WHITE_MASK)

    def piece(self):
        return self.x

    # Return a string representation of the piece. 
    # By default, white pieces are represented by capital letters and
    # black pieces by small letters
    # Convention:
    #	    Rook -> r, R
    #	    Bishop -> b, B
    #	    Knight -> n, N
    #	    King -> k, K
    #	    Queen -> q, Q
    #	    Pawn -> p, P
    def __str__(self):
        retStr = ''

        if self.x & self.MAX_BIT_MASK & self.PAWN:
            retStr = 'p'
        elif self.x & self.MAX_BIT_MASK & self.BISHOP:
            retStr = 'b'
        elif self.x & self.MAX_BIT_MASK & self.KNIGHT:
            retStr = 'n'
        elif self.x & self.MAX_BIT_MASK & self.ROOK:
            retStr = 'r'
        elif self.x & self.MAX_BIT_MASK & self.QUEEN:
            retStr = 'q'
        elif self.x & self.MAX_BIT_MASK & self.KING:
            retStr = 'k'
	elif self.x == self.NO_PIECE:
	    retStr = '.'

	if (self.x & self.BLACK_MASK): 
            return retStr 
        elif not (self.x & self.WHITE_MASK):
            return string.upper(retStr)
	else:
	    return retStr

    # Pieces
    BLACK_PAWN = Piece('black', 'pawn')
    BLACK_BISHOP = Piece('black', 'bishop')
    BLACK_KNIGHT = Piece('black', 'knight')
    BLACK_ROOK = Piece('black', 'rook')
    BLACK_QUEEN= Piece('black', 'queen')
    BLACK_KING = Piece('black', 'king')
    WHITE_PAWN = Piece('white', 'pawn')
    WHITE_BISHOP = Piece('white', 'bishop')
    WHITE_KNIGHT = Piece('white', 'knight')
    WHITE_ROOK = Piece('white', 'rook')
    WHITE_QUEEN= Piece('white', 'queen')
    WHITE_KING = Piece('white', 'king')

# class Pos
class Pos:
    def __init__(self, pos=''):
        self.pos = pos
        self.rank = pos[0]
        self.fil = pos[1]

        self.y = 8 - int(self.fil) 
        self.x = ord(self.rank) - ord('a')

    def __str__(self):
	    return 'x = ' + str(self.x) + ' y = ' + str(self.y)

# Exception IllegalMoveException
class IllegalMoveException(Exception):
    def __init__(self, msg=None):
        Exception.__init__(self, msg)

# class Move
class Move:
    def __init__(self, fromPosStr='', toPosStr=''):
	    # fromPos and toPos are in algebraic notation
	    self.fromPosStr = fromPosStr
	    self.toPosStr = toPosStr
	
	    self.fromPos = None
	    self.toPos = None

	    if (self.fromPosStr):
	        self.fromPos = Pos(self.fromPosStr)
	    if (self.toPosStr):
	        self.toPos = Pos(self.toPosStr)

# class Board
class Board:
    FILES = 'abcdefgh'

    def __init__(self, b=None):
        self.bitmap = [0, 0, 0, 0, 0, 0, 0, 0]
        
        # Normal constructor
        if not b:
            self.board = []

            # Create a blank board
            for i in range(8):
                # Create a blank rank
                rank = []
                for j in range(8):
                    rank.append(None)
                    
                self.board.append(rank)

        # Copy constructor
        else:
            self.board = []

            # Create a blank board
            for i in range(8):
                rank = []
                brank = b[i]
                for j in range(8):
                    piece = brank[j]
                    if piece.piece() != Piece.NO_PIECE:
                        self.bitmap[j] = self.bitmap[j] | (1 << j)
                    rank.append(piece)

                self.board.append(rank)            

    # Set the starting position on the board
    def setStartingPosition(self):
	    # black rooks
        self.setAt(Pos('a8'), BLACK_ROOK)
        self.setAt(Pos('h8'), BLACK_ROOK)

	    # white rooks
        self.setAt(Pos('a1'), WHITE_ROOK)
        self.setAt(Pos('h1'), WHITE_ROOK)

	    # black knights
        self.setAt(Pos('b8'), BLACK_KNIGHT)
        self.setAt(Pos('g8'), BLACK_KNIGHT)

	    # white knights
        self.setAt(Pos('b1'), WHITE_KNIGHT)
        self.setAt(Pos('g1'), WHITE_KNIGHT)

	    # black bishops
	    self.setAt(Pos('c8'), BLACK_BISHOP) 
	    self.setAt(Pos('f8'), BLACK_BISHOP)

	    # white bishops
	    self.setAt(Pos('c1'), WHITE_BISHOP) 
	    self.setAt(Pos('f1'), WHITE_BISHOP)

	    # black king and queen
	    self.setAt(Pos('d8'), BLACK_QUEEN)
	    self.setAt(Pos('e8'), BLACK_KING)

	    # white king and queen
	    self.setAt(Pos('d1'), WHITE_QUEEN)
	    self.setAt(Pos('e1'), WHITE_KING)

	    # black and white pawns
	    for i in range(8):
	        pos1 = Pos(self.FILES[i] + '7')
	        pos2 = Pos(self.FILES[i] + '2')
	        self.setAt(pos1, BLACK_PAWN) 
	        self.setAt(pos2, WHITE_PAWN)


    # Set the piece at the given position on this board
    def setAt(self, pos, piece):
        self.board[pos.y][pos.x] = piece

    # Return a string representation of the board
    def __str__(self):
        s = ''
        for i in range(len(self.board)):
            rank = self.board[i]
            for j in range(len(rank)):
                piece = rank[j]
                if piece:
                    s = s + str(piece) + ' '
                else:
                    s = s + '. '
            s = s + '\n'

	    # Remove the last '\n' and return the string
        return string.strip(s)

    def isCheckMate(self):
	    pass

    def isLegalDraw(self):
	    pass

    def isStaleMate(self):
	    pass

    # Return a list of all legal moves, that 
    def getAllLegalMoves(self, whoseMove):
        moveLst = []

        moveLst.append(self.pawnMoves)
        moveLst.append(self.bishopMoves)
        moveLst.append(self.knightMoves)
        moveLst.append(self.rookMoves)
        moveLst.append(self.queenMoves)
        moveLst.append(self.kingMoves)

        return moveLst

    def newPosition(self, whoseMove, move):
        pass

    def pawnMoves(self):
        lst = []

        # First get all pawn positions
        return lst


    def bishopMoves(self):
        pass

    def knightMoves(self):
        pass

    def rookMoves(self):
        pass

    def queenMoves(self):
        pass

    def kingMoves(self):
        pass

    # Returns true/false based on whether the position on the board is 
    # empty.
    # pos -> Pos object
    def isEmptySquare(self, pos):
        pass

