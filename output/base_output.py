from abc import ABC, abstractmethod
from typing import List


class BaseOutput(ABC):
    """Represents an output device to output the state of the game board"""

    @abstractmethod
    def output_board(self, board_state: List[List[bool]]) -> None:
        """
        Output a single frame of the board.
        :param board_state: The state of the output board.
        """
        ...
