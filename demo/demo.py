# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] editable=true slideshow={"slide_type": "slide"}
# # Demo
#
# ## Question-based Visualizations
#
# ### Weather Data Exploration

# %% [markdown] editable=true slideshow={"slide_type": "slide"}
# ### Context
#
# Metheorological data from the greater alpine region
#
# ![](https://www.zamg.ac.at/histalp/images//subreg_all_large.png)
#

# %% [markdown] editable=true slideshow={"slide_type": "slide"}
# ## Scenario 
# We have aggregated, monthly data.
#
# We want to say something related to:
# * 🌞 Sunshine
# * 🌧️ Rainfall

# %% [markdown] editable=true slideshow={"slide_type": "slide"}
# ## Let's try QBV together!
#
# ---
#
# ### Three Laws of Effective Visual Communication
#
# 1. Have a **clear purpose**
# 1. **Show** the data **clearly**
# 1. Make the **message obvious**
#
#

# %% editable=true slideshow={"slide_type": "slide"}
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import seaborn.objects as so

from magic import *  # for demo only ;)

# %% editable=true slideshow={"slide_type": "slide"}
data.head(3)

# %% editable=true slideshow={"slide_type": ""}
# How are **sunshine** and **rain** related?
# * Is there sunshine, when it is raining?
# * ...
# ---
# How much sunshine in summer?
# Where is sunny or rainy?
# How are sunshien and rainfall related wrt location?

# %%
(
    so.Plot(data=data, x=SUN, y=RAIN)
    .label(title="How are sunshine and rainfall related?\nIs there sunshine, when it is raining?")
    .add(so.Dot(alpha=0.2))
    .add(so.Line(color='r'), so.PolyFit(order=1))
)

# %%
(
    so.Plot(data=data, x=SUN, y=RAIN, color=SEASON)
    .label(title="How are sunshine and rainfall related?\nWe expect a negative correlation.")
    .add(so.Dot(alpha=0.2))
    .add(so.Line(linewidth=5), so.PolyFit(order=1))
)

# %%
(
    so.Plot(data=data, x=SUN, y=RAIN)
    .facet(col=MONTH, wrap=3)
    .label(title="Month: {}".format)
    .add(so.Dot(alpha=0.2))
    .add(so.Line(color='r'), so.PolyFit(order=1))
)
