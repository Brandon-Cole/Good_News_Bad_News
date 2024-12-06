.PHONY: clean all create_db_with_sources_plot headline_analysis report

SHELL := /bin/bash

clean:
	rm -f ./plots/*.png
	rm -rf ./Database/__pycache__
	rm -f ./Database/GNBN.db
	rm -f ./report_generation/report.html

PYTHON = python3

all: create_db_with_sources_plot headline_analysis report

create_db_with_sources_plot: ./Database/GNBN.db ./plots/news_source_distribution.png

./Database/GNBN.db ./plots/news_source_distribution.png: ./Database/create_db.py ./Database/db_utils.py ./data/NewsArticles.csv ./data/headlines_with_embeddings.csv
	cd ./Database && $(PYTHON) create_db.py

headline_analysis: ./plots/headline_embeddings_source_spread.png ./plots/headline_embeddings_tsne_clusters.html

./plots/headline_embeddings_source_spread.png ./plots/headline_embeddings_tsne_clusters.html: ./analysis/cluster_headlines.py ./Database/GNBN.db ./Database/db_utils.py
	cd ./analysis && $(PYTHON) cluster_headlines.py

report: ./report_generation/report.html

./report_generation/report.html: ./report_generation/report.py ./Database/db_diagram.png \
	./report_generation/template.html ./plots/news_source_distribution.png \
	./plots/headline_embeddings_tsne_clusters.html ./plots/headline_embeddings_source_spread.png
	cd ./report_generation && $(PYTHON) report.py
