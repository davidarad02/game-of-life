from time import sleep
from typing import List

from output.base_output import BaseOutput


class Console1FPSOutput(BaseOutput):
    """Represents the console as an output device for the board status, in 1 frame per second."""
    def output_board(self, board_state: List[List[bool]]) -> None:
        for y in range(len(board_state)):
            for x in range(len(board_state[y])):
                print('#' if board_state[y][x] else '_', end=' ')
            print()
        print()
        sleep(1)  # Sleep 1 second to separate two frames.
