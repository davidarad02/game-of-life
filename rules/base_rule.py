from abc import ABC, abstractmethod
from cell_state.base_cell_state import BaseCellState


class BaseRule(ABC):
    """Represents a basic rule to change the board state."""

    @abstractmethod
    def check_cell(self, cell_state: BaseCellState) -> bool:
        """
        Implementation of the rule. Checks if the cell needs to change according to the rule.

        :param cell_state: The state of the current cell.
        :return: A bool that represents whether the cell needs to change its value.
        """
        ...
