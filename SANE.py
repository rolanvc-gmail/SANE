from NE import NeuroEvolution


class SANE(NeuroEvolution):
    def initialize(self):
        raise NotImplementedError()

    def terminate(self):
        raise NotImplementedError()

    def compute_fitness(self):
        raise NotImplementedError()

    def recombine(self):
        raise NotImplementedError()

    def mutate(self):
        raise NotImplementedError()

