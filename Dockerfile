FROM python:3.9-slim
RUN apt-get update && apt-get install -y make
RUN pip install --no-cache-dir pandas numpy matplotlib seaborn plotly scikit-learn scipy jinja2 pickle joypy itertools


