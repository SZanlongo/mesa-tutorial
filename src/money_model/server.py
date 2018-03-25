from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import CanvasGrid, ChartModule

from src.money_model.model import MoneyModel


def agent_portrayal(agent):
    """
    Rendering portrayal of an agent
    :param agent: agent to render
    :return: portrayal dict
    """
    portrayal = {"Shape": "circle",
                 "Filled": "true"
                 }

    if agent.wealth > 0:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.5
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2

    return portrayal


# canvas grid with dimensions 10 x 10, drawn in 500 x 500 pixels
grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

# plot gini
chart = ChartModule([{"Label": "Gini",
                      "Color": "black"
                      }],
                    data_collector_name="datacollector"
                    )

# user-definable number of agents
# parameter changes don't take place until the model is reset
n_slider = UserSettableParameter("slider", "Number of Agents", 100, 2, 200, 1)

# create server
server = ModularServer(MoneyModel,
                       [grid, chart],
                       "Money Model",
                       {"N": n_slider, "width": 10, "height": 10})
server.port = 8521  # default
server.launch()
