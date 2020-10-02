from abc import ABC, abstractmethod


class BaseCellState(ABC):
    """A model that represents the state of a certain cell"""
    def __init__(self, cell_value):
        self._cell_value = cell_value

    def get_cell_value(self) -> bool:
        """Return the read-only value of the cell's value"""
        return self._cell_value

    @abstractmethod
    def living_neighbor_count(self) -> int:
        """Calculate the number of living neighbors of the cell."""
        ...

    @abstractmethod
    def dead_neighbor_count(self) -> int:
        """Calculate the number of dead neighbors of the cell."""
        ...
