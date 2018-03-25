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
        """
        Step through a simulation tick
        """
        self.move()
        if self.wealth > 0:
            self.give_money()

    def move(self):
        """
        Randomly select a neighboring cell and move to it
        """
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,  # neighbors including diagonals
            include_center=False
        )
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def give_money(self):
        """
        Get all agents present in cell and give one of them money
        """
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = random.choice(cellmates)
            self.wealth -= 1
            other.wealth += 1
