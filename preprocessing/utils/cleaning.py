import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class DropColumnTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_new = X.copy()
        X_transformed = X_new.drop(columns=self.columns, axis=1)
        return X_transformed
    
    
class DuplicateRemover(BaseEstimator, TransformerMixin):
    """
    A custom transformer to remove duplicate rows from a pandas DataFrame.

    Methods:
        fit(X, y=None):
            Fit method required by scikit-learn BaseEstimator. Returns self.

        transform(X):
            Transform method to remove duplicate rows from the input DataFrame X.
            Raises a TypeError if X is not a pandas DataFrame.
            Returns a new DataFrame with duplicate rows removed.
    """

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X_new = X.copy()
        if not isinstance(X_new, pd.DataFrame):
            raise TypeError("Input should be a pandas DataFrame")
        return X_new.drop_duplicates()
    
    
class OutlierRemover_IQR(BaseEstimator, TransformerMixin):
    """
    A custom transformer to remove outliers from selected columns of a pandas DataFrame.

    Attributes:
        columns (list): A list of column names to remove outliers from.
        threshold (float, optional): Multiplier for the IQR to define outliers. Default is 1.5.

    Methods:
        fit(X, y=None):
            Fit method required by scikit-learn BaseEstimator. Returns self.

        transform(X, y=None):
            Transform method to remove outliers from the selected columns of the input DataFrame X.
            Computes IQR for selected columns, identifies outliers based on the threshold,
            and returns a new DataFrame with outlier rows removed.
    """

    def __init__(self, columns, threshold=1.5):
        self.threshold = threshold
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_new = X.copy()
        chosen_columns = X_new[self.columns].columns
        Q1 = X_new[chosen_columns].quantile(0.25)
        Q3 = X_new[chosen_columns].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (self.threshold * IQR)
        upper_bound = Q3 + (self.threshold * IQR)
        outlier_mask = ((X_new[chosen_columns] < lower_bound) | (X_new[chosen_columns] > upper_bound)).any(axis=1)
        cleaned_data = X_new[~outlier_mask]
        return cleaned_data
    
    
class DropNaRows(BaseEstimator, TransformerMixin):
    """
    A custom transformer to drop rows with NaN values in specified columns.

    Attributes:
        columns (list): List of column names to check for NaN values.

    Methods:
        fit(X, y=None):
            Fit method required by scikit-learn BaseEstimator. Returns self.

        transform(X):
            Transform method to drop rows with NaN values in the specified columns.
            Returns a new DataFrame with rows containing NaN values removed.
    """
    def __init__(self, columns):
        self.columns = columns
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X.dropna(subset=self.columns)
