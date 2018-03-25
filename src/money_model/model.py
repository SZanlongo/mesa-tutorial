import random

from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import MultiGrid
from mesa.time import RandomActivation

from src.money_model.agent import MoneyAgent
from src.money_model.utilities import compute_gini


class MoneyModel(Model):
    """
    A model with N agents
    """

    def __init__(self, N, width, height):
        self.running = True
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)  # create a toroidal grid
        self.schedule = RandomActivation(self)

        # create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)
            # add agent to random grid cell
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        self.datacollector = DataCollector(
            model_reporters={"Gini": compute_gini},  # A function to call
            agent_reporters={"Wealth": "wealth"}  # An agent attribute
        )

    def step(self):
        """
        Advance the model by 1 step
        """
        self.datacollector.collect(self)
        self.schedule.step()
