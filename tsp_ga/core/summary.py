import os
from typing import List


class GASummary:

    best_result: List=[],
    best_fitness: float=0.0

    def __str__(self):
        return f'''
            {"=" * (os.get_terminal_size().__getattribute__('columns') - 12)}
            The best Result was: {self.best_result}
            The Fitness for it was: {self.best_fitness}
            {"=" * (os.get_terminal_size().__getattribute__('columns') - 12)}
        '''