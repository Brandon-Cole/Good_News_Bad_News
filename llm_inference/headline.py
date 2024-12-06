import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

input_csv_path = "headlines.csv"
output_csv_path = "headlines_with_embeddings.csv"

df = pd.read_csv(input_csv_path)
df.columns = df.columns.str.strip()

with open(output_csv_path, "w") as f:
    f.write("title,subtitle,embedding\n")

print("Processing headlines and generating embeddings...")
for index, row in df.iterrows():
    title = row['title']
    subtitle = row['subtitle']

    try:
        embedding = model.encode(title)
        embedding_str = ",".join(map(str, embedding))

        with open(output_csv_path, "a") as f:
            safe_title = title.replace('"', '""')
            safe_subtitle = subtitle.replace('"', '""') if pd.notna(subtitle) else ""
            f.write(f'"{safe_title}","{safe_subtitle}","{embedding_str}"\n')

        print(f"Processed {index + 1}/{len(df)} headlines")
    except Exception as e:
        print(f"Failed to process headline {index + 1}: {e}")
        continue

print(f"Headlines with embeddings saved to {output_csv_path}")
