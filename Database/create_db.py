from db_utils import Database
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle

harvard_data = pd.read_csv('../data/NewsArticles.csv')
harvard_data = harvard_data.iloc[:, :6]

def source_from_link(link):
    domain_splits = ['.com', '.go', '.ie', '.co']
    if "http://" in link or "https://" in link:
        link = link.split("://")[-1]
        if "www." in link:
            link = link.split("www.")[-1]
        for domain in domain_splits:
            if domain in link:
                return link.split(domain)[0]
    return 'unknown'

harvard_data['source'] = harvard_data['article_source_link'].apply(source_from_link)

embedding_data = pd.read_csv('../data/headlines_with_embeddings.csv')

summary_data = pd.read_csv('../data/articles_summarized_IDs.csv')

summary_embedding_data = pd.read_csv('../data/articles_summarized_IDs_embeddings.csv')

plt.figure(figsize=(12, 6))
harvard_data['source'].value_counts().plot(kind='bar', color='lightgreen', width=0.8)
plt.title('News Source Distribution', fontsize=16, fontweight='bold')
plt.xlabel('News Source', fontsize=14)
plt.xticks(rotation=45, ha= 'right', fontsize=12)
plt.ylabel('Number of Articles', fontsize=14)
plt.tight_layout()
plt.savefig('../plots/news_source_distribution.png')

db = Database('GNBN.db')

db.create_table('articles', """
    article_id INTEGER PRIMARY KEY,
    publish_date TEXT,
    source TEXT,
    text TEXT
""")

db.create_table('sources', """
    article_id INTEGER PRIMARY KEY,
    url TEXT,
    FOREIGN KEY (article_id) REFERENCES articles (article_id)
""")

db.create_table('headlines', """
    article_id INTEGER PRIMARY KEY,
    title TEXT,
    subtitle TEXT,
    embedding BLOB
""")

db.create_table('summaries', """
    summary_ID INTEGER PRIMARY KEY,
    article_ID INTEGER,
    summary TEXT,
    FOREIGN KEY (article_ID) REFERENCES articles (article_id)
""")

db.create_table('summary_embeddings', """
    summary_ID INTEGER PRIMARY KEY,
    embedding BLOB,
    FOREIGN KEY (summary_ID) REFERENCES summaries (summary_ID)
""")


article_data = [
    (row['article_id'], row['publish_date'], row['source'], row['text'])
    for _, row in harvard_data.iterrows()
]

source_data = [
    (row['article_id'], row['article_source_link'])
    for _, row in harvard_data.iterrows()
]

headline_data = []
for _, row in harvard_data.iterrows():
    embedding_row = embedding_data.loc[embedding_data['title'] == row['title'], 'embedding']
    if not embedding_row.empty:
        headline_data.append((row['article_id'], row['title'], row['subtitle'], embedding_row.values[0]))

summary_data = [
    (row['summary_ID'], row['article_id'], row['summary'])
    for _, row in summary_data.iterrows()
]

#handle similar to headline data which just used values[0], dont use pickle
summary_embedding_data_serialized = [
    (row['summary_ID'], row['embedding'])
    for _, row in summary_embedding_data.iterrows()
]
    

db.insert_data('articles', article_data)
db.insert_data('sources', source_data)
db.insert_data('headlines', headline_data)
db.insert_data('summaries', summary_data)
db.insert_data('summary_embeddings', summary_embedding_data_serialized)
db.close()
