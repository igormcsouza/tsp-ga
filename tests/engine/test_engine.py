from tsp_ga import engine
from tsp_ga.engine.types import Chromosome


def test_engine_builder_add_objective_function():
    tsp = engine\
        .TSPGeneticAlgorithmBuilder()\
        .add_objective_function(lambda chromosome: 1.0)

    assert tsp.objective_function != None

def test_engine_builder_add_constraint():
    tsp = engine\
        .TSPGeneticAlgorithmBuilder()\
        .add_constraint(lambda chromosome: True)\
        .add_constraint(lambda chromosome: False)

    assert tsp.constraints != None
    assert len(tsp.constraints) == 2