import matplotlib.pyplot as plt
from mesa.batchrunner import BatchRunner

from src.money_model.model import MoneyModel
from src.money_model.utilities import compute_gini

fixed_params = {"width": 10,
                "height": 10}
variable_params = {"N": range(10, 500, 10)}

batch_run = BatchRunner(MoneyModel,
                        fixed_parameters=fixed_params,
                        variable_parameters=variable_params,
                        iterations=5,
                        max_steps=100,
                        model_reporters={"Gini": compute_gini})
batch_run.run_all()

run_data = batch_run.get_model_vars_dataframe()
print(run_data.head())
plt.scatter(run_data.N, run_data.Gini)
plt.show()
