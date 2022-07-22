# %%
import pandas as pd
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import seaborn as sns
from quickda.explore_data import *
from quickda.clean_data import *
from quickda.explore_numeric import *
from quickda.explore_categoric import *
from quickda.explore_numeric_categoric import *
from quickda.explore_time_series import *

# %%
dataframe = pd.read_csv('train.csv', encoding='latin-1',engine='python')
print(dataframe.head())

profile = ProfileReport(dataframe)
# %%
# %%
print(profile)