from cell_state.base_cell_state import BaseCellState
from rules.base_rule import BaseRule


class LonelinessRule(BaseRule):
    """Represents the loneliness rule - if a living cell has less than two living neighbors, it dies."""
    def check_cell(self, cell_state: BaseCellState) -> bool:
        return cell_state.get_cell_value() and cell_state.living_neighbor_count() < 2
