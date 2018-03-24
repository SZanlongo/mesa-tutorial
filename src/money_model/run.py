from plotly.graph_objs import Histogram, Figure
from plotly.offline import plot

from src.money_model.model import MoneyModel

all_wealths = []
for i in range(100):
    # run the model
    model = MoneyModel(10)
    for i in range(10):
        model.step()

    # store the results
    for agent in model.schedule.agents:
        all_wealths.append(agent.wealth)

fig = Figure(
    data=[Histogram(x=all_wealths,
                    xbins=dict(start=0, size=1, end=len(all_wealths)))]
)
plot(fig, filename='../../output/plots/money_model.html')
