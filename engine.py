from typing import List
from board import Board
from output.base_output import BaseOutput
from rules.base_rule import BaseRule


class Engine:
    """Represents the game engine - running every turn in the game and updating the board."""
    def __init__(self, board: Board, rules: List[BaseRule], output: BaseOutput):
        self._board = board
        self._rules = rules
        self._output = output

    def _run_single_turn(self) -> None:
        """Run a single turn of the game"""
        for y in range(self._board.get_height()):
            for x in range(self._board.get_width()):
                for rule in self._rules:
                    cell_state = self._board.cell_state(x, y)
                    if rule.check_cell(cell_state):
                        self._board.set_cell(x, y, not cell_state.get_cell_value())
                        break  # A cell can only be changed once per turn
        self._board.flush_board()

    def run_game(self, max_turn_count=None) -> None:
        """Start running the game."""
        turn_count = 0
        while not max_turn_count or max_turn_count < turn_count:
            self._output.output_board(self._board.get_board_state())
            self._run_single_turn()
