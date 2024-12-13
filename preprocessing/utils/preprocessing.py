import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class DataTypeTransformer(BaseEstimator, TransformerMixin):
    """
    A custom transformer to change the datatype of specified columns in a DataFrame.
    
    Attributes:
        columns (dict): A dictionary where keys are column names and values are the target data types
                        (e.g., {'column1': 'datetime64', 'column2': 'category'}).
    """
    def __init__(self, columns: dict):
        self.columns = columns
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X_new = X.copy()
        for col, dtype in self.columns.items():
            try:
                if dtype == "datetime64":
                    X_new[col] = pd.to_datetime(X_new[col])
                elif dtype == "category":
                    X_new[col] = X_new[col].astype("category")
                else:
                    X_new[col] = X_new[col].astype(dtype)
            except Exception as e:
                raise ValueError(f"Error converting column {col} to {dtype}: {e}")
        return X_new