from tsp_ga.dataset import read_data, preprocess_data
from tsp_ga.dataset.preprocessors import data_to_list, take_header
from tsp_ga.engine.types import Chromosome
from tsp_ga.dataset.types import Data
from tsp_ga.engine import TSPGeneticAlgorithmBuilder

def main():
    raw_data = read_data('data/usa115475.tsp')
    data = preprocess_data(raw_data, [lambda d: take_header(d, 7), data_to_list])

    def obj_func(chromosome: Chromosome, data: Data) -> float:
        def euclidian_distance(a, b):
            return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

        d = sum([euclidian_distance(data[i-1], data[i]) for i in range(len(data))])

        return d

    def non_repetitive(chromosome: Chromosome) -> bool:
        _set = set(chromosome)
        return len(chromosome) != len(_set)

    model = TSPGeneticAlgorithmBuilder.instantiate()\
        .setup_genes({'n_genes': len(data)})\
        .add_objective_function(obj_func)\
        .add_constraint(non_repetitive)\
        .build()

    result = model.fit()

    print(result)
