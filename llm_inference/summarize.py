import pandas as pd
from llama_cpp import Llama

model_path = "Phi-3-medium-128k-instruct-Q4_K_M.gguf"

llm = Llama.from_pretrained(
    repo_id="bartowski/Phi-3-medium-128k-instruct-GGUF",
    filename=model_path,
    n_ctx=128000
)

def summarize(text: str, max_output_tokens=150) -> str:
    try:
        response = llm.create_chat_completion(
            messages=[
                {"role": "user", "content": f"Summarize the following text into one concise sentence:\n\n{text}"}
            ],
            max_tokens=max_output_tokens
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"An error occurred while summarizing: {e}")
        return "Error occurred during summarization."

csv_path = "articles.csv"
df = pd.read_csv(csv_path)
df.columns = df.columns.str.strip()

output_csv_path = "articles_summarized.csv"

with open(output_csv_path, "w") as f:
    f.write("article_id,summary\n")

for index, row in df.iterrows():
    print(f"Processing row {index + 1} of {len(df)}...")
    article_id = row['article_id']
    text = row['text']
    summary = summarize(text)
    with open(output_csv_path, "a") as f:
        safe_summary = summary.replace('"', '""')
        f.write(f'"{article_id}","{safe_summary}"\n')

print(f"Summarized content saved to {output_csv_path}")
