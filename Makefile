
DB_FILE = my_database.db
INTERMEDIATE_DIR = intermediate_data
PLOTS_DIR = plots
REPORT = report.tex 
PDF_REPORT = report.pdf  


all: $(PLOTS_DIR)/text_content_clusters.png $(PLOTS_DIR)/headline_clusters.png $(PDF_REPORT)


$(PLOTS_DIR)/text_content_clusters.png: $(DB_FILE) | $(INTERMEDIATE_DIR) $(PLOTS_DIR)
    @echo "Generating text_content_clusters.png using data from $(DB_FILE)..."
    python generate_text_content_clusters.py $(DB_FILE) $(INTERMEDIATE_DIR)/data1.csv
    python plot_data.py $(INTERMEDIATE_DIR)/data1.csv $(PLOTS_DIR)/text_content_clusters.png
    @echo "text_content_clusters.png generated."


$(PLOTS_DIR)/headline_clusters.png: $(DB_FILE) | $(INTERMEDIATE_DIR) $(PLOTS_DIR)
    @echo "Generating headline_clusters.png using data from $(DB_FILE)..."
    python generate_headline_clusters.py $(DB_FILE) $(INTERMEDIATE_DIR)/data2.csv
    python plot_data.py $(INTERMEDIATE_DIR)/data2.csv $(PLOTS_DIR)/headline_clusters.png
    @echo "headline_clusters.png generated."


$(PDF_REPORT): $(REPORT) $(PLOTS_DIR)/text_content_clusters.png $(PLOTS_DIR)/headline_clusters.png
    @echo "Generating LaTeX report from $(REPORT)..."
    pdflatex $(REPORT)  
    @echo "LaTeX report generated as $(PDF_REPORT)."


$(INTERMEDIATE_DIR):
    mkdir -p $(INTERMEDIATE_DIR)


$(PLOTS_DIR):
    mkdir -p $(PLOTS_DIR)


.PHONY: clean
clean:
    @echo "Cleaning up intermediate data and plots..."
    rm -rf $(INTERMEDIATE_DIR)/*
    rm -rf $(PLOTS_DIR)/*
    rm -f $(PDF_REPORT)  
    @echo "Cleanup complete."
