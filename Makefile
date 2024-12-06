.PHONY: clean all create_db_with_sources_plot headline_analysis report

SHELL := /bin/bash

clean:
	rm -f ./plots/*.png
	rm -f ./plots/*.html
	rm -rf ./Database/__pycache__
	rm -f ./Database/GNBN.db
	rm -f ./report_generation/report.html

PYTHON = python3

all: create_db_with_sources_plot headline_analysis text_analysis headline_text_comparison report

create_db_with_sources_plot: ./Database/GNBN.db ./plots/news_source_distribution.png

./Database/GNBN.db ./plots/news_source_distribution.png: ./Database/create_db.py ./Database/db_utils.py \
	./data/NewsArticles.csv ./data/headlines_with_embeddings.csv ./data/articles_summarized_IDs.csv \
	./data/articles_summarized_IDs_embeddings.csv
	cd ./Database && $(PYTHON) create_db.py

headline_analysis: ./plots/headline_embeddings_source_spread.png ./plots/headline_embeddings_tsne_clusters.html

./plots/headline_embeddings_source_spread.png ./plots/headline_embeddings_tsne_clusters.html: ./analysis/cluster_headlines.py ./Database/GNBN.db \
	./Database/db_utils.py
	cd ./analysis && $(PYTHON) cluster_headlines.py

text_analysis: ./plots/summary_embeddings_tsne_clusters.html ./plots/summary_embeddings_source_spread.png

./plots/summary_embeddings_tsne_clusters.html ./plots/summary_embeddings_source_spread.png: ./analysis/cluster_content.py ./Database/GNBN.db \
	./Database/db_utils.py
	cd ./analysis && $(PYTHON) cluster_content.py

headline_text_comparison: ./plots/headline_summary_distance_distribution.png ./plots/t_test_results.html

./plots/headline_summary_distance_distribution.png ./plots/t_test_results.html: ./analysis/compare_headline_content.py ./Database/GNBN.db \
    ./Database/db_utils.py
	cd ./analysis && $(PYTHON) compare_headline_content.py

report: ./report_generation/report.html

./report_generation/report.html: ./report_generation/report.py ./Database/db_diagram.png \
	./report_generation/template.html ./plots/news_source_distribution.png \
	./plots/headline_embeddings_tsne_clusters.html ./plots/headline_embeddings_source_spread.png \
	./plots/summary_embeddings_tsne_clusters.html ./plots/summary_embeddings_source_spread.png \
	./plots/headline_summary_distance_distribution.png ./plots/t_test_results.html
	cd ./report_generation && $(PYTHON) report.py
