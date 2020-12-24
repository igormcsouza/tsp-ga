from .types import ObjectiveFunction, Constraints, Constraint


class TSPGeneticAlgorithm:

    def __init__(
        self, objective_function: ObjectiveFunction=None, constraints: Constraints=[]):

        self.objective_function = objective_function
        self.constraints = constraints

class TSPGeneticAlgorithmBuilder:
    
    def __init__(
        self, objective_function: ObjectiveFunction=None, constraints: Constraints=[]):

        self.objective_function = objective_function
        self.constraints = constraints

    @staticmethod
    def instantiate():
        return TSPGeneticAlgorithmBuilder

    def add_objective_function(self, objective_function: ObjectiveFunction):
        self.objective_function = objective_function
        return self

    def add_constraint(self, constraint: Constraint):
        self.constraints.append(constraint)
        return self