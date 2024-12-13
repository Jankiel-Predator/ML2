import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math


def boxplots(dataset: pd.DataFrame, columns: list):
    """
    Creates vertical boxplots for specified columns in a dataset.

    Args:
        dataset: The DataFrame containing the data.
        columns: A list of column names to include in the boxplots.
    """
    data = dataset[columns]
    melted_data = data.melt(var_name='Feature', value_name='Value')
    
    #feature_mapping = {col: col for col in columns}
    #melted_data['Feature'] = melted_data['Feature'].map(feature_mapping)
    
    plt.figure(figsize=(12, 6))
    sns.boxplot(
        data=melted_data,
        x='Feature',
        y='Value',
        palette='viridis',
        hue='Feature'
    )
    plt.ylabel('Value', fontsize=12)
    plt.xlabel(None)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    
    
def histograms(dataset: pd.DataFrame, columns: list):
    """
    Constructs histograms for the specified columns in the dataset.

    Args:
        dataset: The DataFrame containing the data.
        columns: A list of column names for which to create histograms.

    Returns:
        None: Displays the histograms.
    """
    num_columns = len(columns)
    rows = math.ceil(num_columns / 2)
    
    fig, axes = plt.subplots(rows, 2, figsize=(9, rows * 3))
    axes = axes.flatten() # type: ignore
    
    i = 0
    for i, column in enumerate(columns):
        sns.histplot(data=dataset, x=column, kde=True, ax=axes[i], palette=sns.color_palette("viridis", as_cmap=True))
        axes[i].set_title(f'{column}', fontsize=14)
        axes[i].set_xlabel(None)
        if i % 2 == 0:
            axes[i].set_ylabel('Frequency', fontsize=12)
        else:
            axes[i].set_ylabel(None)
    
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
    
    plt.tight_layout()
    plt.show()


def barplots(dataset: pd.DataFrame, columns: list):
    """
    Creates barplots for specified columns in the dataset, arranged two per row.
    
    Args:
        dataset: The DataFrame containing the data.
        columns: A list of column names for which to create the barplots.
    """
    num_plots = len(columns)
    nrows = (num_plots + 1) // 2
    fig, axes = plt.subplots(nrows=nrows, ncols=2, figsize=(12, 6 * nrows))
    axes = axes.flatten() # type: ignore

    for i, column in enumerate(columns):
        sns.barplot(hue=dataset[column].value_counts().index,
                    y=dataset[column].value_counts().values,
                    ax=axes[i],
                    palette="viridis")
        
        axes[i].set_title(f'{column}')
        axes[i].set_xlabel(None)
        axes[i].set_ylabel('Frequency')
    
    if num_plots % 2 != 0:
        fig.delaxes(axes[-1])
    
    plt.tight_layout()
    plt.show()


def correlations(dataset, columns):
    """
    Displays a correlation matrix heatmap for the selected features in the dataset.

    Args:
        dataset: The DataFrame containing the data.
        columns: A list of column names for which to calculate the correlation matrix.

    Returns:
        None: Displays the heatmap.
    """
    corr_matrix = dataset[columns].corr()

    sns.heatmap(
        corr_matrix, 
        annot=True, 
        fmt=".2f", 
        cmap="viridis",
        linewidths=0.5, 
        cbar=True
    )
    plt.xticks(fontsize=6, rotation=45)
    plt.yticks(fontsize=6, rotation=0)
    plt.tight_layout()
    plt.show()


def pairplots(dataset, columns, hue=None):
    """
    Constructs pairplots for the selected features in the dataset.

    Args:
        dataset: The DataFrame containing the data.
        columns: A list of column names for which to create pairplots.
        hue: Optional; column name to use for color-coding the pairplots.

    Returns:
        None: Displays the pairplots.
    """
    g = sns.pairplot(dataset[columns], hue=hue, palette="viridis", corner=True)
    for ax in g.axes.flatten():
        if ax is not None:
            ax.set_xlabel(ax.get_xlabel())
            ax.set_ylabel(ax.get_ylabel())
    plt.show()
