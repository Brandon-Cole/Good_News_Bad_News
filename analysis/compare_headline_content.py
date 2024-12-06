import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from scipy import stats
from joypy import joyplot
from itertools import combinations

# Ensure the database utility module is included
db_utils_dir = os.path.abspath('../Database')
if db_utils_dir not in sys.path:
    sys.path.append(db_utils_dir)

from db_utils import Database

# Connect to the database
db = Database('../Database/GNBN.db')

# Query for headline embeddings and article IDs
query_headlines = """
    SELECT h.embedding, a.source, h.article_id
    FROM headlines h
    JOIN articles a ON h.article_id = a.article_id
"""
data_headlines = db.execute(query_headlines)

# Query for summary embeddings and article IDs
query_summaries = """
    SELECT se.embedding, a.source, s.article_id
    FROM summary_embeddings se
    JOIN summaries s ON se.summary_id = s.summary_id
    JOIN articles a ON s.article_id = a.article_id
"""
data_summaries = db.execute(query_summaries)

db.close()

# Extract data
headline_embeddings, headline_sources, headline_article_ids = zip(*data_headlines)
summary_embeddings, summary_sources, summary_article_ids = zip(*data_summaries)

# Convert embeddings from strings to numpy arrays
headline_embeddings = np.array([
    np.fromstring(e, sep=",") if isinstance(e, str) else np.fromstring(e.decode(), sep=",")
    for e in headline_embeddings
])
summary_embeddings = np.array([
    np.fromstring(e, sep=",") if isinstance(e, str) else np.fromstring(e.decode(), sep=",")
    for e in summary_embeddings
])

# Create dictionaries to map article IDs to their embeddings and sources
headline_embeddings_dict = dict(zip(headline_article_ids, zip(headline_embeddings, headline_sources)))
summary_embeddings_dict = dict(zip(summary_article_ids, zip(summary_embeddings, summary_sources)))

# Find common article IDs
common_article_ids = set(headline_embeddings_dict.keys()) & set(summary_embeddings_dict.keys())

# Calculate distances and store sources
article_distances = {}
article_sources = {}

for article_id in common_article_ids:
    headline_embedding, headline_source = headline_embeddings_dict[article_id]
    summary_embedding, summary_source = summary_embeddings_dict[article_id]
    distance_value = distance.euclidean(headline_embedding, summary_embedding)
    article_distances[article_id] = distance_value
    article_sources[article_id] = headline_source  # Assuming source is the same for headline and summary

# Convert the results to a DataFrame
distance_df = pd.DataFrame({
    'article_id': list(article_distances.keys()),
    'distance': list(article_distances.values()),
    'source': [article_sources[article_id] for article_id in article_distances.keys()]
})

# Calculate mean distance for each source and sort by it
source_mean_distances = distance_df.groupby('source')['distance'].mean().sort_values().index
distance_df['source'] = pd.Categorical(distance_df['source'], categories=source_mean_distances, ordered=True)
distance_df = distance_df.sort_values(by='source')

# Plotting with joyplot and pastel color scheme
plt.figure(figsize=(14, 8))
joyplot(
    data=distance_df,
    by='source',
    column='distance',
    figsize=(14, 8),
    title='Distribution of Distances Between Headline and Summary Embeddings by Source',
    colormap=plt.cm.Pastel1,
    linewidth=1,
    alpha=0.8
)
plt.savefig('../plots/headline_summary_distance_distribution.png')
plt.show()

# Calculate t-tests between all unique source pairs
sources = distance_df['source'].unique()
results = []

for source1, source2 in combinations(sources, 2):
    group1 = distance_df[distance_df['source'] == source1]['distance']
    group2 = distance_df[distance_df['source'] == source2]['distance']
    t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)
    results.append((source1, source2, t_stat, p_value))

# Create a DataFrame to display the results as a table
results_df = pd.DataFrame(results, columns=['Source 1', 'Source 2', 't-statistic', 'p-value'])

# Display the results table
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
results_df = results_df.sort_values(by='p-value')
print(results_df)

# Save the results table to an HTML file
results_df.to_html('../plots/t_test_results.html', index=False)
