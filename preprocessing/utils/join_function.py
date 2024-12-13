import pandas as pd

def join_dataframes(dfs, join_keys_map):
    """
    Perform a join on multiple dataframes with groupby aggregation, handling different key names.

    Parameters:
    - dfs: List of pandas DataFrames to join.
    - join_keys_map: List of dictionaries, where each dictionary maps the join keys in the
      current dataframe to a common key name (e.g., [{'df_key': 'common_key'}, ...]).

    Returns:
    - A pandas DataFrame after performing the join with the specified aggregation rules.
    """
    if len(dfs) != len(join_keys_map):
        raise ValueError("Each dataframe must have a corresponding key mapping.")

    # Standardize the join keys in each dataframe
    standardized_dfs = []
    for i, (df, key_map) in enumerate(zip(dfs, join_keys_map)):
        standardized_df = df.rename(columns=key_map)
        standardized_df = standardized_df.add_suffix(f"_{i}")  # Add suffix to avoid column name collisions
        standardized_df.rename(columns={f"{list(key_map.values())[0]}_{i}": list(key_map.values())[0]}, inplace=True)
        standardized_dfs.append(standardized_df)

    # Use the standardized join keys for all joins
    common_keys = list(join_keys_map[0].values())

    # Function to handle aggregation for groupby
    def aggregate(group):
        result = {}
        for col in group.columns:
            if col in common_keys:
                continue  # Skip join keys
            if pd.api.types.is_numeric_dtype(group[col]):
                result[col] = group[col].mean()  # Numeric columns: mean
            else:
                result[col] = group[col].mode().iloc[0] if not group[col].mode().empty else None  # Non-numeric: most frequent
        return pd.Series(result)

    # Start with the first dataframe
    merged_df = standardized_dfs[0]

    # Iteratively join and aggregate
    for i in range(1, len(standardized_dfs)):
        temp_df = pd.merge(merged_df, standardized_dfs[i], on=common_keys, how='outer')
        merged_df = temp_df.groupby(common_keys).apply(aggregate).reset_index()

    return merged_df.dropna()