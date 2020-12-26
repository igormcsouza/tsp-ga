from .types import ObjectiveFunction, Constraints, Constraint, GeneSetup
from ..core.summary import GASummary


class TSPGeneticAlgorithm:

    def __init__(
        self, gene_setup: GeneSetup={}, 
        objective_function: ObjectiveFunction=None, 
        constraints: Constraints=[]):

        self.gene_setup = gene_setup
        self.objective_function = objective_function
        self.constraints = constraints

    def fit(
        self, generations: int=0, init_pop: int=10, offspring: int=2, 
        crossover_method='one_point', 
        multation_chance: float=10.0) -> GASummary:

        summary = GASummary()

        # Init Population
        # Calc fitness
        # Mating Pool (High chance if high fitness)
        # Select parents (Random Bias Based)
        # Crossover + Mutation
        # Generate Offsprint
        # Until generations (if == 0, until treshold)

        summary.best_fitness = 10
        summary.best_result = [1, 2, 3]

        return summary

class TSPGeneticAlgorithmBuilder:
    
    def __init__(
        self, gene_setup: GeneSetup={}, 
        objective_function: ObjectiveFunction=None, 
        constraints: Constraints=[]):

        self.gene_setup = gene_setup
        self.objective_function = objective_function
        self.constraints = constraints

    @staticmethod
    def instantiate():
        return TSPGeneticAlgorithmBuilder()

    def setup_genes(self, gene_setup: GeneSetup):
        self.gene_setup.update(gene_setup)
        return self

    def add_objective_function(self, objective_function: ObjectiveFunction):
        self.objective_function = objective_function
        return self

    def add_constraint(self, constraint: Constraint):
        self.constraints.append(constraint)
        return self
    
    def build(self):
        instance = TSPGeneticAlgorithm(
            self.gene_setup, self.objective_function, self.constraints)

        return instance