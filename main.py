"""
Conway's game of life - a simulation of life of cells on a board, according to rules.
"""
from board import Board
from engine import Engine
from output.console_1fps_output import Console1FPSOutput
from rules.loneliness_rule import LonelinessRule
from rules.population_explosion_rule import PopulationExplosionRule
from rules.repopulation_rule import RepopulationRule


def main():
    initial_board = [  # A basic glider pattern: https://en.wikipedia.org/wiki/Glider_(Conway%27s_Life)
        [False, True, False, False, False],
        [False, False, True, False, False],
        [True, True, True, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
    ]
    board = Board(initial_board)
    rules = [
        LonelinessRule(),
        PopulationExplosionRule(),
        RepopulationRule()
    ]
    output = Console1FPSOutput()
    engine = Engine(board, rules, output)
    engine.run_game()


if __name__ == '__main__':
    main()
