import pandas as pd
from pandas.core.frame import DataFrame
from os.path import join, dirname

customers: DataFrame = pd.read_csv(
    join(dirname(__file__), 'data', 'olist_customers_dataset.csv'))
customers.head()
