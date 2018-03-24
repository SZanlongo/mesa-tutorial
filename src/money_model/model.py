from mesa import Model
from mesa.time import RandomActivation

from src.money_model.agent import MoneyAgent


class MoneyModel(Model):
    """
    A model with N agents
    """

    def __init__(self, N):
        self.schedule = RandomActivation(self)
        self.num_agents = N
        # create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

    def step(self):
        """
        Advance the model by 1 step
        """
        self.schedule.step()
