from copy import deepcopy
from typing import List

from cell_state.base_cell_state import BaseCellState
from cell_state.cell_state_2d import CellState2D


class Board:
    """Represents the 'game of life' board."""
    def __init__(self, initial_board: List[List[bool]]):
        """
        Initializes the Board object.

        `_board` is the status of the board in the current turn.
        When reading the status of the board, it should be from `board`.

        `_working_board` is the board that should be changed according to the rules.

        When the current turn is over, `_board` should be set to `_working_board` using `flush_board`.

        :param initial_board: The initial state of the board.
        """
        self._board = initial_board
        self._working_board = deepcopy(initial_board)

        self._height = len(self._board)
        if self._height > 0:
            self._width = len(self._board[0])
        else:
            self._width = 0

    @classmethod
    def empty_board(cls, width: int, height: int):
        """
        Generate a new, empty board with a certain height and width.

        :param width: The width of the board.
        :param height: The height of the board.
        :return: A Board object with all empty cells.
        """
        return cls([[False] * width for _ in range(height)])

    def cell_state(self, x: int, y: int) -> BaseCellState:
        """
        Generate a cell state model representing the state of the cell in x,y.

        :param x: The x coordinate of the cell.
        :param y: The y coordinate of the cell.
        :return: A CellState2D model of the state of the cell.
        """
        cells = []
        if x > 0:
            cells.append(self._board[y][x-1])
            if y > 0:
                cells.append(self._board[y-1][x-1])
        if y > 0:
            cells.append(self._board[y-1][x])
            if x < self._width - 1:
                cells.append(self._board[y-1][x+1])
        if x < self._width - 1:
            cells.append(self._board[y][x+1])
            if y < self._height - 1:
                cells.append(self._board[y+1][x+1])
        if y < self._height - 1:
            cells.append(self._board[y+1][x])
            if x > 0:
                cells.append(self._board[y+1][x-1])
        state = CellState2D(self._board[y][x], cells)
        return state

    def set_cell(self, x: int, y: int, value: bool) -> None:
        """
        Set the value of a cell on the working board.

        :param x: The x coordinate of the cell.
        :param y: The y coordinate of the cell.
        :param value: The value to be set to cell.
        """
        self._working_board[y][x] = value

    def flush_board(self) -> None:
        """Flush the current state of `_working_board` to `_board`, to get it ready for the next turn."""
        self._board = deepcopy(self._working_board)

    def get_height(self) -> int:
        """
        :return: The read-only value of the board height.
        """
        return self._height

    def get_width(self) -> int:
        """
        :return: The read-only value of the board width.
        """
        return self._width

    def get_board_state(self) -> List[List[bool]]:
        """
        :return: The read-only value of the entire board.
        """
        return self._board
