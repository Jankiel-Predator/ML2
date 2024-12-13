import pandas as pd


def missing_values(dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Checks for missing values in a DataFrame.

    Args:
        dataset: Dataframe to be examined.

    Returns:
        pd.Series: A Pandas Series containing the number of missing values for each column.
    """
    miss_val = dataset.isnull().sum()
    missing_values_df = pd.DataFrame({"Column": miss_val.index, 
                                      "Missing Values": miss_val.values})
    
    return missing_values_df


def duplicates(dataset: pd.DataFrame, exclude = None):
    """
    Checks for duplicates in a DataFrame, with an option to exclude certain columns from the check.

    Args:
        dataset: DataFrame to be examined.
        exclude: List of column names to exclude from the duplication check. Default is None.

    Returns:
        pd.DataFrame or None: A DataFrame containing the duplicated rows, or None if no duplicates are found.
    """
    dataset = dataset.copy()
    if exclude:
        dataset_to_check = dataset.drop(columns=exclude)
    else:
        dataset_to_check = dataset
    
    duplicated_rows = dataset[dataset_to_check.duplicated()]
    
    if not duplicated_rows.empty:
        return duplicated_rows
    else:
        print("There are no duplicates.")
        return None
    
    
def summarize(dataset: pd.DataFrame):
    """
    Summarizes a DataFrame by returning two descriptive statistics DataFrames.
    
    Args:
        dataset: The DataFrame to be summarized.
    
    Returns:
        tuple: A tuple containing two DataFrames:
            - One with summary statistics for numeric columns.
            - One with summary statistics for object (categorical) columns.
    """
    numeric_summary = dataset.describe().T
    object_summary = dataset.describe(include=['O']).T
    
    return numeric_summary, object_summary


def nunique_values(dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame with the number of unique values for each column in the dataset.
    Additionally, includes a 'Unique Values' column showing the unique categories if there 
    are less than 10 unique values, or 'Too Much' if there are 10 or more unique values.
    The 'Unique Values' column will be omitted if all columns have 'Too Much' as the value.

    Args:
        dataset: The DataFrame containing the data.

    Returns:
        pd.DataFrame: A DataFrame with columns 'Column', 'Nunique', and optionally 'Unique Values'.
    """
    unique_counts = dataset.nunique()
    unique_values = []
    
    for column in dataset.columns:
        if unique_counts[column] <= 10:
            unique_values.append(dataset[column].unique())
        else:
            unique_values.append("Too Much")

    result_df = pd.DataFrame({
        'Column': unique_counts.index,
        'Nunique': unique_counts.values,
        'Unique Values': unique_values
    })
    
    if all(isinstance(value, str) and value == "Too Much" for value in unique_values):
        result_df = result_df.drop(columns=["Unique Values"])

    return result_df


def outliers(dataset: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Identifies the number of outliers in the specified columns of a DataFrame using the IQR method
    and calculates the percentage of outliers out of the total number of rows.

    Args:
        dataset: The DataFrame containing the data.
        columns: A list of column names to analyze for outliers.

    Returns:
        pd.DataFrame: A DataFrame containing the count of outliers and their percentage for each column.
    """
    outlier_counts = {}
    total_rows = len(dataset)

    for column in columns:
        if pd.api.types.is_numeric_dtype(dataset[column]):
            Q1 = dataset[column].quantile(0.25)
            Q3 = dataset[column].quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = dataset[(dataset[column] < lower_bound) | (dataset[column] > upper_bound)]
            count = len(outliers)
            percentage = (count / total_rows) * 100
            
            outlier_counts[column] = (count, percentage)
        else:
            outlier_counts[column] = (None, None)

    outliers_df = pd.DataFrame(
        [(col, count, perc) for col, (count, perc) in outlier_counts.items()],
        columns=["Column", "Outlier Count", "Outlier Percentage (%)"]
    )
    
    outliers_sorted = outliers_df.sort_values("Outlier Count", ascending=False)
    return outliers_sorted.set_index("Column")
