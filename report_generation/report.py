from jinja2 import Template
import datetime

template_path = "template.html"
output_path = "report.html"

data = {
    "title": "AI-Driven News Study",
    "subtitle": "All The Analysis That's Fit To Print",
    "date": datetime.datetime.now().strftime("%B %d, %Y"),
    "sections": [
        {
            "heading": "Work Summary",
            "text": "Research has shown that individuals can experience heightened emotions without even reading entire news stories.<sup>1</sup> This study aimed to analyze headlines to identify patterns among news sources and assess the degree of misleading content. The analysis revealed potential trends in the way popular news outlets craft headlines, often using sensational or biased language to attract attention. This research sought to mitigate the potential impact of such headlines on public perception and emotional responses, emphasizing the need for critical engagement with news media to foster better information processing and understanding.",
            "figures": []
        },
        {
            "heading": "Methodology",
            "text": 
        "The study used a dataset of ~ 4,000 news articles from a Harvard University dataset for NLP-tasks. "
        "The data was cleaned and loaded into an SQLite database, which was normalized to Third Normal Form (3NF) to minimize redundancy and ensure efficient retrieval and update operations." 
        "The headlines were then retrieved and embedded using jinaai/jina-embeddings-v3. "
        "This model had ~ 572 million parameters and embedding size of 1024. Following some initial clustering analysis, "
        "I ended up using all-MiniLM-L6-v2 instead which contains 23M parameters and an output dimension of 384. "
        "The embeddings were then visualized using t-SNE to identify patterns in the data. Pairwise Euclidean distances "
        "were calculated to assess the similarity of headlines by source."
        "The text was then summarized with a large-context window model, specifically the Phi-3-medium-128k-instruct-Q4_K_M"
        "model. This model was quantized to 4 bits to reduce the model size and inference time. The summaries were generated with"
        "max 150 tokens and a minimum length of 50 tokens. The summaries were then compared to the original text to assess the quality of the summaries.",
            "figures": [
                {
                    "type": "image",
                    "src": "../Database/db_diagram.png",
                    "caption": "Database Schema"
                }
            ]
        },


        {
            "heading": "Visual Insights",
            "text": "Here we examine the distribution of news sources in the dataset (Figure 1) and visualize trends in headline embeddings (Figure 2). We further investigated the average pairwise Euclidean distance between headlines by source (Figure 3).",
            "figures": [
                {
                    "type": "image",
                    "src": "../plots/news_source_distribution.png",
                    "caption": "Figure 1: Distribution of Dataset by Source."
                },
                {
                    "type": "html",
                    "html": "<iframe src='../plots/headline_embeddings_tsne_clusters.html'></iframe>",
                    "caption": "Figure 2: Interactive Visualization of News Headlines."
                },
                {
                    "type": "image",
                    "src": "../plots/headline_embeddings_source_spread.png",
                    "caption": "Figure 3: Average Pairwise Euclidean Distance Between Headlines By Source."
                }
            ]
        },
        {
            "heading": "References",
            "text": """
            1. Mousoulidou, M., Taxitari, L., & Christodoulou, A. (2024). Social Media News Headlines and Their Influence on Well-Being: Emotional States, Emotion Regulation, and Resilience. European journal of investigation in health, psychology and education, 14(6), 1647–1665. https://doi.org/10.3390/ejihpe14060109<br>
            2. News Source 2<br>
            3. News Source 3
            """,
            "figures": []
        }
    ]
}

with open(template_path, "r") as file:
    template = Template(file.read())

rendered_html = template.render(data)

with open(output_path, "w") as output_file:
    output_file.write(rendered_html)
