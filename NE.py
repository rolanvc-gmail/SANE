# This implements Neuroevolution through the NE class.

from abc import ABC, abstractmethod

class NeuroEvolution(ABC):
    def run(self):
        self.initialize()
        while not self.terminate():
            self.compute_fitness()
            self.recombine()
            self.mutate()

    @abstractmethod
    def initialize(self):
        raise NotImplementedError()

    @abstractmethod
    def terminate(self):
        raise NotImplementedError()

    @abstractmethod
    def compute_fitness(self):
        raise NotImplementedError()

    @abstractmethod
    def recombine(self):
        raise NotImplementedError()

    @abstractmethod
    def mutate(self):
        raise NotImplementedError()


