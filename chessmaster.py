#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" sChess Piece Legal move"""

import time

# Task # 1: Position of a piece

class ChessPiece(object):
    """ Set moves /position for chess piece

    Args:
        position(alphanumeric): stores tile notation of current position
        move(list): stores stores info of moves taken in form of tuples

    Attr:
        prefix(empty): empty class attribute

    """

    prefix = ''         # class attribute


    def __init__(self, position):
        """ Instane for ChessPiece class checks legality of move + move itself

        """

        self.position = position
        self.moves = []

        if ChessPiece.is_legal_move(self, position): # legal move
            self.position = position
        else:                                         # illegal move
            excep = '`{}`is not a legal start position'
            ValueError(excep.format(position))


    def algebraic_to_numeric(self, tile):
        """Class function. Determines legal move for chess piece.
            Keeping track of x,y coordinate positio of piece.
            This conversion will help us determine legal moves for
            our chess pieces.

        Arg:
            tile(str): Input string value of cordinates

        Returns:
            tuple:as of  x and y coordinates


        Examples:
            >>> piece.algebraic_to_numeric('j9')
            False
            >>> piece.algebraic_to_numeric('e7')
            (4, 6)
        """
        # board = 64 tiles: x axis a to h and Y axis 1 to 8 or 0 to 7

        x_coord = 'abcdefgh'

        y_coord = [1, 2, 3, 4, 5, 6, 7, 8]
        
        if tile[0] in x_coord and int(tile[1]) in y_coord:  # if found on board
            return (x_coord.find(tile[0]), (int(tile[1]) - 1)) # return position

        else:
            return False

    def is_legal_move(self, position):
        """Determine converted move is legal/legality of new move.

        Arg:
            position: possible move on board

        Attribute:
            new_move(int): move conveted to nemeric position

        Returns:
            bool: True /False depanding if move is legal/illegal
        """
        new_move = self.algebraic_to_numeric
        if new_move(position):
            return True
        else:
            return False


    def move(self, position):
        """ Function to move a piece to a new position on board.
            Afte testing if move is legal by calling is_legal_move function
            if legal postiion attribute  value updated to new position value.

        """
        new_move = self.is_legal_move(position) # check legality of move

        # if move is legal create tuple (oldposition, newposition, timestamp)
        # prior to tuple,  prepend `prefix` class attribute to two positions

        if new_move:
            position_tuple = (self.prefix + self.position,
                              self.prefix + position, time.time())

            self.moves.append(position_tuple)   # add move to all moves listing

            self.position = position            # current position

            return position_tuple

        else:
            return False


# Task # 2 : Rook move any number of houses along the x-axis or the y-axis
class Rook(ChessPiece):
    """ Class for rook , sub class of ChessPiece, inheriting functions for
    new, next moves. Legal move has additional condition + tile on board

    Args:
        position(alphanumeric): position on the board
    Attribute:
    prefix(str):default set to 'R'
    """

    prefix = 'R'

    def __init__(self, position):   # override

        ChessPiece.__init__(self, position)

    def is_legal_move(self, position): # legal move for rook
        """Rook subclass check legality

        Args:
            position: Legal move on board

        Returns:
            bool: True or false for legal/illegal move
        """
        if ChessPiece.is_legal_move(self, position):
            if self.position[0] is position[0]:
                if int(self.position[1]) != int(position[1]):
                    return True
            else:
                if int(self.position[1]) == int(position[1]):
                    return True
        else:
            return False




if __name__ == '__main__':
    PIECE = ChessPiece('a1')
    print 'Piece position'
    print PIECE.position
    print 'Algebraic to Numeric'
    print 'j9 ', PIECE.algebraic_to_numeric('j9')
    print 'e7 ', PIECE.algebraic_to_numeric('e7')
    print 'Piece move'
    print 'j9 ', PIECE.move('j9')
    print 'a1 ', PIECE.move('a1')
    print 'e7 ', PIECE.move('e7')
    print 'Rook'
    PIECE_ROOK = Rook('a1')
    print 'prefix ', PIECE_ROOK.prefix
    print 'Rook Move'
    print 'b2 ', PIECE_ROOK.move('b2')
    print 'h8 ', PIECE_ROOK.move('h8')
