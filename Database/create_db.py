from db_utils import Database
import pandas as pd
import matplotlib.pyplot as plt


harvard_data = pd.read_csv('data/NewsArticles.csv')
harvard_data = harvard_data.iloc[:, :6]

def source_from_link(link):
    """Obtain news source from hyperlink

    Parameters
    ----------
    link : str
        The hyperlink to the news article

    Returns
    -------
    str
        The news source extracted from the hyperlink (i.e, ABC News, CNN, etc.)
    """
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


plt.figure(figsize=(10, 8))
harvard_data['source'].value_counts().plot(kind='bar', color='skyblue')
plt.title('News Source Distribution')
plt.xlabel('News Source')
plt.ylabel('Number of Articles')
plt.savefig('plots/news_source_distribution.png')


db = Database('GNBN.db')

columns = """
    article_id INTEGER PRIMARY KEY,
    publish_date TEXT,
    article_source_link TEXT,
    title TEXT,
    subtitle TEXT,
    text TEXT,
    source TEXT
"""

db.create_table('articles', columns)
sql_data = [tuple(row) for row in harvard_data.values]

db.insert_data('articles', sql_data)
db.close()


