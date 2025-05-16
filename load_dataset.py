import pandas as pd

# Column names based on the dataset documentation
columns = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
]

# To load the dataset
df = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',
    header=None, names=columns, na_values=' ?', skipinitialspace=True
)

# To drop rows with missing values
df.dropna(inplace=True)

# To preview
df.head()
