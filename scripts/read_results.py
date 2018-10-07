# -*- coding: utf-8 -*-
"""
Minimalist example file showing how to read the results of a Dispa-SET run

@author: Sylvain Quoilin
"""

# Change directory to the root folder of Dispa-SET:
import os
os.chdir('..')

# Import Dispa-SET
import DispaSET as ds

# Load the inputs and the results of the simulation
inputs,results = ds.get_sim_results(path='Simulations/simulationWB_2015_Standard',cache=True)

# if needed, define the plotting range for the dispatch plot:
#import pandas as pd
#rng = pd.date_range(start='2015-05-10',end='2015-05-24',freq='h')

# Generate country-specific plots
ds.plot_country(inputs,results)
#ds.plot_country(inputs,results,rng=rng,c=('HR'))


# Bar plot with the installed capacities in all countries:
cap = ds.plot_country_capacities(inputs)

# Bar plot with the energy balances in all countries:
ds.plot_energy_country_fuel(inputs,results,ds.get_indicators_powerplant(inputs,results))

# Analyse the results for each country and provide quantitative indicators:
r = ds.get_result_analysis(inputs,results)

