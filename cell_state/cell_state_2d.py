from typing import List
from cell_state.base_cell_state import BaseCellState

CELL_COUNT = 8


class CellState2D(BaseCellState):
    """A model that represents the state of a certain cell in a 2D board."""
    def __init__(self, cell_value, neighbors: List[bool]):
        """
        :param cell_value: The current value of the cell.
        :param neighbors: A list of booleans representing the neighbors.
        Should only contain eight values.
        """
        super().__init__(cell_value)
        self._neighbors = neighbors

    def living_neighbor_count(self) -> int:
        return sum(self._neighbors)

    def dead_neighbor_count(self) -> int:
        return CELL_COUNT - self.living_neighbor_count()
