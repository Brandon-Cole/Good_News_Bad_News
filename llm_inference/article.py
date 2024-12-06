import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

input_csv_path = "articles_summarized_IDs.csv"
output_csv_path = "articles_summarized_IDs_embeddings.csv"

df = pd.read_csv(input_csv_path)
df.columns = df.columns.str.strip()

with open(output_csv_path, "w") as f:
    f.write("summary_ID,embedding\n")

print("Processing summaries and generating embeddings...")
for index, row in df.iterrows():
    summary_ID = row['summary_ID']
    summary = row['summary']

    try:
        embedding = model.encode(summary)
        embedding_str = ",".join(map(str, embedding))

        with open(output_csv_path, "a") as f:
            f.write(f'{summary_ID},"{embedding_str}"\n')

        print(f"Processed {index + 1}/{len(df)} summaries")
    except Exception as e:
        print(f"Failed to process summary {index + 1}: {e}")
        continue

print(f"Summaries with embeddings saved to {output_csv_path}")
