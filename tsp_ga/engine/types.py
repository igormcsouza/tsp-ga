from typing import Callable, Tuple, List


Gene = Tuple[float, float]
Chromosome = List[Gene]
ObjectiveFunction = Callable[[Chromosome], float]
Constraint = Callable[[Chromosome], bool]
Constraints = List[Constraint]