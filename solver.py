# Hello World program in Python

from enum import Enum


class EdgeDef:
    def __init__(self, shape, innie):
        self.shape = shape
        self.innie = innie
        self.outie = not innie

    def full_name(self):
        return "{}-{}".format(self.shape, "In" if self.innie else "Out")

    def short_name(self):
        return "{}{}".format(self.shape[:1], "I" if self.innie else "O")


class Shape:
    Heart = "Heart"
    Diamond = "Diamond"
    Club = "Club"
    Spade = "Spade"


class Edge:
    HeartOut = EdgeDef(Shape.Heart, False)
    DiamondOut = EdgeDef(Shape.Diamond, False)
    SpadeOut = EdgeDef(Shape.Spade, False)
    ClubOut = EdgeDef(Shape.Club, False)
    HeartIn = EdgeDef(Shape.Heart, True)
    DiamondIn = EdgeDef(Shape.Diamond, True)
    SpadeIn = EdgeDef(Shape.Spade, True)
    ClubIn = EdgeDef(Shape.Club, True)


class Piece:
    def __init__(self, n, a, b, c):
        self.edge = (a, b, c)
        self.number = n
        self.rotate_count = 0

    def rotate(self):
        self.edge = (self.edge[1], self.edge[2], self.edge[0])

    def display(self):
        return "{}: [{}, {}, {}]".format(self.number, self.edge[0].full_name(), self.edge[1].full_name(), self.edge[2].full_name())


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
    return edge1.shape == edge2.shape and edge1.innie == edge2.outie


def print_board():
    # output:
    #     /    \
    # D-Out   C-Out
    #  /          \
    #  -- Spade ---

    for row_index in range(len(board)):
        row = board[row_index]

        for col_row in range(4):
            spaces = 14 * (3 - row_index)

            if spaces > 0:
                for x in range(spaces):
                    print(" ", end="")

            for column_index in range(len(row)):
                piece = row[column_index]

                if piece is None:
                    left = "lf"
                    right = "rh"
                    bottom = "bo"
                    number = 0
                else:
                    left = piece.edge[0].short_name()
                    right = piece.edge[1].short_name()
                    bottom = piece.edge[2].short_name()
                    number = piece.number

                if (row_index % 2 == 0 and column_index % 2 == 0) or (row_index % 2 == 1 and column_index % 2 == 0):
                    if col_row == 0:
                        print("     /  \\     ", end="")
                    elif col_row ==1:
                        print("   {} {:0>2d}  {}  ".format(left, number, right), end="")
                    elif col_row == 2:
                        print("  /        \\  ", end="")
                    elif col_row == 3:
                        print(" ---- {} ---- ".format(bottom), end="")
                else:
                    if col_row == 0:
                        print(" ---- {} ---- ".format(left), end="")
                    elif col_row == 1:
                        print("  \\         / ", end="")
                    elif col_row == 2:
                        print("  {}  {:0>2d}  {}  ".format(bottom, number, right), end="")
                    elif col_row == 3:
                        print("    \\   /     ", end="")

            print()


def go(my_pieces, my_row_index):
    if my_row_index == 0:
        my_edge = 2
        other_edge = 0
    elif my_row_index == 1:
        my_edge = 1
        other_edge = 2
    else:
        print("Row index {} not defined".format(my_row_index))
        return False

    remaining_pieces = my_pieces

    found = False

    for my_row_slot in range(len(board[my_row_index])):
        found = False

        if board[my_row_index][my_row_slot] is not None:
            continue

        for my_piece_index in range(len(remaining_pieces)):
            remaining_pieces = []

            my_piece = my_pieces[my_piece_index]

            board[my_row_index][my_row_slot] = my_piece

            found = False

            if len(board[my_row_index]) > my_row_slot + 1 and board[my_row_index][my_row_slot + 1] is not None:
                # see if my piece fits
                print("Finding edge match")

                for rotate in range(3):
                    if edge_fits(my_piece.edge[my_edge], board[my_row_index][my_row_slot + 1].edge[other_edge]):
                        found = True
                        break
                    my_piece.rotate()
                other_piece_index = -1
            else:
                for other_piece_index in range(len(my_pieces)):
                    if other_piece_index == my_piece_index:
                        continue

                    other_piece = my_pieces[other_piece_index]
                    if edge_fits(my_piece.edge[my_edge], other_piece.edge[other_edge]):
                        print("Match: row:{} slot:{} edge:{} {} == {}".format(my_row_index, my_row_slot, my_edge,
                                                                              my_piece.display(), other_piece.display()))
                        board[my_row_index + 1][my_row_slot + 1] = other_piece
                        found = True
                        break
            if not found:
                continue

            print_board()

            for i in range(len(my_pieces)):
                if i != my_piece_index and i != other_piece_index:
                    remaining_pieces.append(my_pieces[i])

            break

    go(remaining_pieces, my_row_index + 1)

    return found


# print_board()

go(pieces, 0)
