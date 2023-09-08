# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# Here are our necessary imports, using code from the [Altair docs](https://altair-viz.github.io/altair-tutorial/notebooks/01-Cars-Demo.html).

# %%
import altair as alt

# load a simple dataset as a pandas DataFrame
from vega_datasets import data
cars = data.cars()
cars.head()

# %% [markdown]
# When we execute the cell above, we see the first several rows of the dataset.
#
# Now, execute the cell below to create an Altair chart.

# %%
chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()
chart

# %% [markdown]
# Don't worry if you get a warning about `FutureWarning: the convert_dtype parameter is deprecated and will be removed in a future version`.
