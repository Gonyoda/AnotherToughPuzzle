# Hello World program in Python

from enum import Enum;


class Edge(Enum):
    HeartOut = "HeartOut"
    DiamondOut = "DiamondOut"
    ClubOut = "ClubOut"
    SpadeOut = "SpadeOut"
    HeartIn = "HeartIn"
    DiamondIn = "DiamondIn"
    ClubIn = "ClubIn"
    SpadeIn = "SpadeIn"


class Piece:
    def __init__(self, n, a, b, c):
        self.side = (a, b, c)
        self.number = n
        self.rotate_count = 0

    def rotate(self):
        self.side = (self.side[1], self.side[2], self.side[0])

    def display(self):
        return "{}: [{}, {}, {}]".format(self.number, self.side[0], self.side[1], self.side[2])


pieces = (
    Piece(1, Edge.HeartOut, Edge.DiamondOut, Edge.SpadeIn),
    Piece(2, Edge.SpadeIn, Edge.HeartOut, Edge.ClubIn),
    Piece(3, Edge.DiamondOut, Edge.SpadeOut, Edge.HeartIn),
    Piece(4, Edge.ClubOut, Edge.SpadeOut, Edge.HeartIn),
    Piece(5, Edge.ClubIn, Edge.DiamondOut, Edge.SpadeIn),
    Piece(6, Edge.DiamondOut, Edge.HeartIn, Edge.ClubOut),
    Piece(7, Edge.SpadeOut, Edge.DiamondIn, Edge.ClubIn),
    Piece(8, Edge.HeartIn, Edge.ClubOut, Edge.SpadeIn),
    Piece(9, Edge.ClubIn, Edge.HeartOut, Edge.DiamondIn),
    Piece(10, Edge.DiamondOut, Edge.SpadeOut, Edge.ClubIn),
    Piece(11, Edge.HeartOut, Edge.HeartOut, Edge.DiamondIn),
    Piece(12, Edge.HeartOut, Edge.HeartIn, Edge.DiamondOut),
    Piece(13, Edge.ClubOut, Edge.HeartIn, Edge.SpadeIn),
    Piece(14, Edge.DiamondIn, Edge.SpadeOut, Edge.HeartIn),
    Piece(15, Edge.ClubOut, Edge.SpadeOut, Edge.DiamondIn),
    Piece(16, Edge.DiamondIn, Edge.HeartOut, Edge.SpadeIn)
)

board_pieces_per_row = (1, 3, 5, 7)

board = [
    [None],
    [None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None, None, None],
]


def edge_fits(edge1, edge2):
    if edge1 == Edge.HeartIn and edge2 == Edge.HeartOut:
        return True
    if edge1 == Edge.DiamondIn and edge2 == Edge.DiamondOut:
        return True
    if edge1 == Edge.ClubIn and edge2 == Edge.ClubOut:
        return True
    if edge1 == Edge.SpadeIn and edge2 == Edge.SpadeOut:
        return True
    if edge2 == Edge.HeartIn and edge1 == Edge.HeartOut:
        return True
    if edge2 == Edge.DiamondIn and edge1 == Edge.DiamondOut:
        return True
    if edge2 == Edge.ClubIn and edge1 == Edge.ClubOut:
        return True
    if edge2 == Edge.SpadeIn and edge1 == Edge.SpadeOut:
        return True
    return False


def go(my_pieces, my_row_index):
    if my_row_index == 0:
        my_edge = 2
    if my_row_index == 1:
        my_edge = 1
    print("my_pieces {}".format(len(my_pieces)))

    pieces_on_my_row = board_pieces_per_row[my_row_index]
    my_row = []
    my_row_slot = 0

    for my_piece_index in range(len(my_pieces)):
        remaining_pieces = []

        my_piece = my_pieces[my_piece_index]

        my_row[my_row_slot] = my_piece

        found = False

        for other_piece_index in range(len(my_pieces)):
            if other_piece_index == my_piece_index:
                continue

            other_piece = my_pieces[other_piece_index]
            if edge_fits(my_piece.side[my_edge], other_piece.side[0]):
                print("Match: row:{} slot:{} edge:{} {} == {}".format(my_row_index, my_row_slot, my_edge,
                                                                      my_piece.display(), other_piece.display()))
                board[my_row_index + 1][my_row_slot + 1] = other_piece
                found = True
                break

        for i in range(len(my_piece_index)):
            if i != my_piece_index and i != other_piece_index:
                remaining_pieces.append(my_pieces[i])

        go(remaining_pieces, my_row_index + 1)

        break


go(pieces, [], 0)
