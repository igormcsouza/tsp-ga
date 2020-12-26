from typing import Callable, Tuple, List, Dict, Any


Gene = int
GeneSetup = Dict[str, Any]
Chromosome = List[Gene]
ObjectiveFunction = Callable[[Chromosome, Dict[str, Any]], float]
Constraint = Callable[[Chromosome], bool]
Constraints = List[Constraint]