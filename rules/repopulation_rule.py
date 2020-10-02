from cell_state.base_cell_state import BaseCellState
from rules.base_rule import BaseRule


class RepopulationRule(BaseRule):
    """Represents the repopulation rule - if a dead cell has three living neighbors, it lives."""
    def check_cell(self, cell_state: BaseCellState) -> bool:
        return not cell_state.get_cell_value() and cell_state.living_neighbor_count() == 3
