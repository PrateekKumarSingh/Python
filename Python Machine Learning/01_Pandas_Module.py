# pandas - a powerful data analysis and manipulation library for Python
# =====================================================================

# **pandas** is a Python package providing fast, flexible, and expressive data
# structures designed to make working with "relational" or "labeled" data both
# easy and intuitive. It aims to be the fundamental high-level building block for
# doing practical, **real world** data analysis in Python. Additionally, it has
# the broader goal of becoming **the most powerful and flexible open source data
# analysis / manipulation tool available in any language**. It is already well on
# its way toward this goal


import pandas as pd

# making a data frame
data = {'col1': [1, 2], 'col2': [3, 4], 'col3': [4, 2]}  # data as dictionary
dataframe = pd.DataFrame(data=data)  # converting it dataframe

print("DATAFRAME \n", dataframe)
print("\nOnly COLUMN1,3 data\n", dataframe[['col1','col3']])  # filtering out and accessing columns

# making new column in data frame
dataframe['col4'] = dataframe['col1'] * dataframe['col2']
print(dataframe)


