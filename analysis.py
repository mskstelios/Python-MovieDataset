import matplotlib.pyplot as plt
import numpy as np


def dataset_analysis(data, column, num_of_items):
    values = data[column].value_counts().head(num_of_items)
    labels = values.index
    counts = values.values
    titles = labels.tolist()
    title_indices = np.arange(len(titles))

    plt.figure(figsize=(10, 6))
    plt.bar(title_indices, counts, color='skyblue')
    plt.xlabel('Movie Titles', fontsize=12)
    plt.ylabel('Number of Occurrences', fontsize=12)
    plt.title(f'{num_of_items} Movies by {column.capitalize()}', fontsize=14, pad=15)
    plt.xticks(title_indices, titles, rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()