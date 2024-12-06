import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.manifold import TSNE
from scipy.spatial import distance

db_utils_dir = os.path.abspath('../Database')
if db_utils_dir not in sys.path:
    sys.path.append(db_utils_dir)

from db_utils import Database

db = Database('../Database/GNBN.db')

query = """
    SELECT se.summary_id, se.embedding, s.summary, a.source
    FROM summary_embeddings se
    JOIN summaries s ON se.summary_id = s.summary_id
    JOIN articles a ON s.article_id = a.article_id
"""
data = db.execute(query)
db.close()

summary_IDs, embeddings, summaries, sources = zip(*data)

embeddings = np.array([
    np.fromstring(e, sep=",") if isinstance(e, str) else np.fromstring(e.decode(), sep=",")
    for e in embeddings
])

tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
reduced_embeddings = tsne.fit_transform(embeddings)

plot_df = pd.DataFrame({
    'x': reduced_embeddings[:, 0],
    'y': reduced_embeddings[:, 1],
    'source': sources,
    'Summary': summaries
})

fig_tsne = px.scatter(
    plot_df,
    x='x',
    y='y',
    color='source',
    title='Summary Embeddings Clustering by Source (t-SNE)',
    labels={'x': 't-SNE-1', 'y': 't-SNE-2', 'source': 'Source'},
    hover_data={
        'Summary': True,
        'source': False,
        'x': False,
        'y': False
    },
    opacity=0.7,
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig_tsne.update_traces(
    hoverlabel=dict(
        font_size=10,
        font_family="Verdana"
    )
)

fig_tsne.update_traces(marker=dict(size=10))

fig_tsne.update_layout(
    paper_bgcolor='white',
    plot_bgcolor='white'
)
fig_tsne.write_html('../plots/summary_embeddings_tsne_clusters.html')

unique_sources = plot_df['source'].unique()
source_distances = {}

for source in unique_sources:
    source_data = plot_df[plot_df['source'] == source]
    source_embeddings = source_data[['x', 'y']].values
    pairwise_distances = [distance.euclidean(source_embeddings[i], source_embeddings[j])
                          for i in range(len(source_embeddings))
                          for j in range(i + 1, len(source_embeddings))]
    mean_distance = np.mean(pairwise_distances)
    source_distances[source] = mean_distance

sorted_distances = dict(sorted(source_distances.items(), key=lambda item: item[1], reverse=True))

plt.figure(figsize=(12, 6))
sns.barplot(x=list(sorted_distances.keys()), y=list(sorted_distances.values()), color='pink')
plt.xlabel('Source', fontsize=14)
plt.ylabel('Mean Pairwise Distance', fontsize=14)
plt.title('Spread of Article Text Embeddings by Source', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.tight_layout()
plt.savefig('../plots/summary_embeddings_source_spread.png')
