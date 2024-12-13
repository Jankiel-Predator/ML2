from sklearn.base import BaseEstimator, TransformerMixin

class FeatureAdder(BaseEstimator, TransformerMixin):
    """
    A custom transformer to create a new feature.
    
    Attributes:
        new_feature_name (str): Name of the new feature to be added.
        transform_func (callable): Function to calculate the new feature. 
                                   Takes the input DataFrame and returns a Series.
    """
    def __init__(self, new_feature_name, transform_func):
        self.new_feature_name = new_feature_name
        self.transform_func = transform_func

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_new = X.copy()
        X_new[self.new_feature_name] = self.transform_func(X_new)
        return X_new