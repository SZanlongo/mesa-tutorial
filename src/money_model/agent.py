import random

from mesa import Agent


class MoneyAgent(Agent):
    """
    Agent with fixed initial wealth
    """

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def step(self):
        # print(self.unique_id)
        if self.wealth == 0:
            return

        other_agent = random.choice(self.model.schedule.agents)
        self.wealth -= 1
        other_agent.wealth += 1
