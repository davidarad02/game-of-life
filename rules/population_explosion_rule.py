from cell_state.base_cell_state import BaseCellState
from rules.base_rule import BaseRule


class PopulationExplosionRule(BaseRule):
    """Represents the Population explosion rule - if a living cell has more than three living neighbors, it dies."""
    def check_cell(self, cell_state: BaseCellState) -> bool:
        return cell_state.get_cell_value() and cell_state.living_neighbor_count() > 3
